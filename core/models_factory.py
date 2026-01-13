from models.package import Package
from models.truck import Truck
from models.route import Route
from models.customer import Customer
from models.city_distances import CityDistances



class ModelsFactory:
    def __init__(self,city_distances:CityDistances, route_id = None, package_id=None):
        self._route_id = (route_id+1) if route_id else 1
        self._package_id = (package_id+1) if package_id else 1 
        self._city_distances: CityDistances = city_distances

    def create_package(self, start_location, end_location, weight, customer)->Package:
        package_id = self._package_id
        self._package_id += 1
        return Package(package_id, start_location, end_location, weight, customer)

    def create_route(self,locations)->Route:
        route_id = self._route_id
        self._route_id+=1
        return Route(route_id, locations, self._city_distances)

    def create_customer(self, first_name, last_name, email)->Customer:
        return Customer(first_name, last_name, email)



