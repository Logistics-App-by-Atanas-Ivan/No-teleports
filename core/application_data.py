from models.package import Package
from datetime import datetime
from models.route import Route
from models.truck import Truck
from core.models_factory import ModelsFactory
from models.city_distances import CityDistances
from models.user import User


class ApplicationData:
    def __init__(self):
        self._routes: list[Route] = []
        self._packages: list[Package] =[]
        self._users: list[User] = []
        self._trucks: list[Truck] = ModelsFactory.create_truck()
        self._city_distances: CityDistances = CityDistances()

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

            if route.location_eta(start_location)<datetime.now():
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
    
    def find_truck(self, truck_id: int) -> Truck:
        for truck in self._trucks:
            if truck.truck_id == truck_id:
                return truck

    def find_route(self, route_id: int) -> Route:
        for route in self.routes:
            if route.route_id == route_id:
                return route

    def assign_package(self, package: Package, route: Route):
        #   def calculate_distance(self, start_location, end_location, route):

        distance = self._city_distances.calculate_distance(package.end_location, route)
        travel_time = distance / 87



        

        route.assign_package(package)


        