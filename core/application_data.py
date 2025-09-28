from models.package import Package
from datetime import datetime, timedelta, time
from models.route import Route
from models.truck import Truck
from models.city_distances import CityDistances
from models.user import User
from models.constants.status import Status
from models.customer import Customer

class ApplicationData:
    def __init__(self):
        self._routes: list[Route] = []
        self._packages: list[Package] =[]
        self._users: list[User] = [self._create_initial_manager()] # email, first_name, last_name, password, role
        self._logged_user = None
        self._customers: list[Customer] = []
        self._trucks: list[Truck] = self._create_truck()
        self._city_distances: CityDistances = CityDistances()

    @staticmethod
    def _create_initial_manager():
        user = User('manager1@telerikacademy.com', 'Pesho', 'Peshov', '123456', 'Manager')
        return user
        

    @staticmethod
    def _create_truck()->list[Truck]:
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
    
    # Read-only views
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
    def customers(self):
        return (tuple(self._customers))
    
    @property
    def trucks(self):
        return tuple(self._trucks)
    
    # Authentication
    @property
    def has_logged_in_user(self):
        return self._logged_user is not None
    
    @property
    def logged_in_user(self):
        if self.has_logged_in_user:
            return self._logged_user
        else:
            raise ValueError('There is no logged in user.')       

    def login(self, user: User):
        self._logged_user = user

    def logout(self):
        self._logged_user = None 
    
    # Users
    def create_user(self, email, firstname, lastname, password, user_role) -> User:
        if len([u for u in self._users if u.email == email]) > 0:
            raise ValueError(
                f'User with email {email} already exist. Choose a different email!')

        user = User(email, firstname, lastname, password, user_role)
        self._users.append(user)
        return user
        
    def find_user(self, email) -> User:
        for user in self._users:
            if user.email == email:
                return user
        raise ValueError(f'There is no user with email {email}!')

    #Customers
    def add_customer(self, customer: Customer):
        self._customers.append(customer)

    def find_customer(self, email) -> Customer:
        for customer in self._customers:
            if customer.email == email:
                return customer    

    #Packages
    def add_package(self, package):
        self._packages.append(package)

    def find_package(self, package_id: int)->Package:
        for package in self._packages:
            if package.package_id == package_id:
                return package
        raise ValueError(f'Package with ID {package_id} does not exist!')

    def view_all_unassigned_packages(self):
        packages =[]
        for unassigned_package in self._packages:
            if unassigned_package.status==Status.UNASSIGNED:
                packages.append(unassigned_package)
        return packages

    def view_unassigned_packages_at_location(self, location: str) -> dict[str, int]:
        unassigned_packages = {}
        for package in self._packages:
            if package.start_location == location and package.status == Status.UNASSIGNED:
                    unassigned_packages = self.loads_per_location(package, unassigned_packages)
        return unassigned_packages
    
    def loads_per_location(self, package: Package, dict: dict[str, int]) -> dict[str, int]:
        loads_per_location = dict.copy()
        if package.end_location in loads_per_location:
            loads_per_location[package.end_location] += package.weight
        else:
            loads_per_location[package.end_location] = package.weight
        return loads_per_location 

    #Routes
    def add_route(self, route: Route):
        self._routes.append(route)

    def find_route(self, route_id: int) -> Route:
        for route in self.routes:
            if route.route_id == route_id:
                return route

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
    
    def find_active_routes(self)->list[Route]:
        active_routes=[]
        for route in self.routes:

            if route.departure_time and route.departure_time< datetime.now() +timedelta(hours=24)<route.location_eta(route.locations[-1]):
                active_routes.append(route)
        return active_routes
    
    #Trucks
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
    

    def to_dict(self):
        return {
            'routes': [r.to_dict() for r in self.routes],
            'packages': [p.to_dict() for p in self.packages],
            'users': [u.to_dict() for u in self.users],
            'logged_user' : self.logged_in_user.to_dict() if self.has_logged_in_user else None,
            'customers': [c.to_dict() for c in self.customers],
            'trucks' : [t.to_dict() for t in self.trucks],
        }
    
    @classmethod
    def from_dict(cls, data, city_distances: CityDistances):
        app_data = cls()
        app_data.routes = [Route.from_dict(r,city_distances) for r in data.get('routes', [])]
        app_data.packages = [Package.from_dict(p) for p in data.get('packages', [])]
        app_data.users = [User.from_dict(u) for u in data.get('users', [])]
        app_data.login(data['logged_user'])
        app_data.customers = [Customer.from_dict(c) for c in data.get('customers', [])]
        app_data._trucks = [Truck.from_dict(t) for t in data['trucks']]
        
        if data.get("logged_in_user"):
            app_data.logged_in_user = User.from_dict(data["logged_in_user"])
        return app_data

