from models.package import Package
from datetime import datetime, timedelta, time
from models.route import Route
from models.truck import Truck
from core.models_factory import ModelsFactory
from models.city_distances import CityDistances
from models.user import User
from models.constants.status import Status
from models.customer import Customer


class ApplicationData:
    def __init__(self):
        self._routes: list[Route] = []
        self._packages: list[Package] =[]
        self._users: list[User] = []
        self._customers: list[Customer] = []
        self._trucks: list[Truck] = self.create_truck()
        self._city_distances: CityDistances = CityDistances()

    @staticmethod
    def create_truck()->list[Truck]:
        # id, brand, capacity, range
        trucks = []
        for id in range(1001,1041):
            if id<1011:
                trucks.append(Truck(id,'Scania',42000,8000))
            elif id<1026:
                trucks.append(Truck(id,'Man',37000,10000))
            else:
                trucks.append(Truck(id,'Actros',26000,13000))
        return trucks       

    @property
    def routes(self):
        return tuple(self._routes)
    @property
    def packages(self):
        return tuple(self._packages)
    @property
    def users(self):
        return tuple(self._users)
    @property
    def trucks(self):
        return tuple(self._trucks)

    
    def find_user(self, email) -> User:
        for user in self._users:
            if user.email == email:
                return user

    def add_package(self, package):
        self._packages.append(package)

    def find_package(self, package_id: int)->Package:
        for package in self._packages:
            if package.package_id == package_id:
                return package
            
    def find_existing_route(self, package: Package) -> list[Route]:
        start_location = package.start_location
        end_location = package.end_location
        available_routes =[]

        for route in self._routes:
            if route.assigned_truck is None:
                continue

            if start_location not in route.locations:
                continue

            if self.location_eta(route, start_location)<datetime.now():
            # route.location_eta(start_location)<datetime.now():
                continue

            if end_location not in route.locations:
                continue

            start_location_index = route.locations.index(start_location)
            end_location_index = route.locations.index(end_location)

            if end_location_index<start_location_index:
                continue
            
            if route.free_capacity_at_location(package) is None:
                continue

            available_routes.append(route)
        
        return available_routes
    
    def find_truck(self, route: Route) -> Truck:
        route_total_distance = self._city_distances.calculate_distance(route.locations[-1], route)

        suitable_truck = None
        for truck in self._trucks:
            if truck.truck_range >= route_total_distance:
                if truck.available_from <= datetime.combine(datetime.today().date() + timedelta(days=1), time(hour=6)):
                    return truck
                elif not suitable_truck or truck.available_from < suitable_truck.available_from:
                    suitable_truck = truck
        return suitable_truck

    def find_route(self, route_id: int) -> Route:
        for route in self.routes:
            if route.route_id == route_id:
                return route

    def assign_package(self, package: Package, route: Route):
        package.package_eta = self.eta_calculation(package.end_location, route)
        route.assign_package(package)


    def assign_truck(self, route: Route, truck: Truck):
        route.assigned_truck = truck
        route_final_location = route.locations[-1]
        # final_location_eta = route.location_eta(route_final_location)
        final_location_eta = self.location_eta(route, route_final_location)
        truck.available_from = final_location_eta
        if truck.available_from <= datetime.combine(datetime.today().date() + timedelta(days=1), time(hour=6)): 
            route.departure_time = datetime.combine(datetime.today().date() + timedelta(days=1), time(hour=6))
        else:
            route.departure_time = datetime.combine(truck.available_from.date() + timedelta(days=1), time(hour=6))

    def location_eta(self, route: Route, location)->datetime:
        if location == route.locations[0]:
            return route.departure_time
        location_eta = self.eta_calculation(location, route)
        return location_eta

    def eta_calculation(self, location, route: Route) -> datetime:
        distance = self._city_distances.calculate_distance(location, route)
        travel_time_in_minutes = timedelta(minutes=(distance / 87) * 60)
        return route.departure_time + travel_time_in_minutes
    
    def add_route(self, route: Route):
        self._routes.append(route)

    def view_unassigned_packages(self, location: str) -> dict:
        unassigned_packages = {}
        for package in self._packages:
            if package.start_location == location:
                    unassigned_packages = self.loads_per_location(package, unassigned_packages)
        return unassigned_packages
    
    def bulk_assign_at_location(self, route: Route, location: str) -> dict:
        loads_per_location = {}
        next_locations = route.locations[route.locations.index(location):]
        for package in self._packages:
            if package.status == Status.UNASSIGNED:
                if package.start_location == location and package.end_location in next_locations:
                    if route.free_capacity_at_location(package):
                        self.assign_package(package)                      
                        loads_per_location = self.loads_per_location(package, loads_per_location)
        return loads_per_location

    def loads_per_location(self, package: Package, dict: dict) -> dict:
        loads_per_location = dict.copy()
        if package.end_location in loads_per_location:
            loads_per_location[package.end_location] += package.weight
        else:
            loads_per_location[package.end_location] = package.weight
        return loads_per_location

    def bulk_assign(self, route, location, packages):
        next_locations = route.locations[route.locations.index(location):]
        for package in packages:
            if package.status == Status.UNASSIGNED:
                if package.start_location == location and package.end_location in next_locations:
                    pass
    
    def find_customer(self, email) -> Customer:
        for customer in self._customers:
            if customer.email == email:
                return customer
    
    def add_customer(self, customer: Customer):
        self._customers.append(customer)