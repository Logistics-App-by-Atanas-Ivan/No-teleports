# from models.category import Category
# from models.product import Product
# from models.shampoo import Shampoo
# from models.shopping_cart import ShoppingCart
# from models.toothpaste import Toothpaste
from models.package import Package
from datetime import datetime
from models.route import Route


class ApplicationData:
    def __init__(self):
        self._routes: list[Route] = []
        self._packages: list[Package] =[]
        self._users = []

    
    def user_exists(self, email):
        pass

    def add_package(self, package):
        self._packages.append(package)

    def find_package(self, package_id: int)->Package:
        for package in self._packages:
            if package.package_id == package_id:
                return package
            
    def find_existing_route(self, package: Package):
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

            available_routes.append(route)
        
        return available_routes



            






    

