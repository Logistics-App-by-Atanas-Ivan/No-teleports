from models.package import Package
from models.truck import Truck
from models.route import Route


class ModelsFactory:
    def __init__(self):
        self._route_id = 1
        self._package_id = 1
        # self._trucks = self._create_truck()

    def create_package(self, start_location, end_location, weight, user)->Package:
        package_id = self._package_id
        self._package_id += 1
        return Package(package_id, start_location, end_location, weight, user)

    def create_route(self,*locations)->Route:
        route_id = self._route_id
        self._route_id+=1
        return Route(route_id, *locations)

    def create_user(self, email):
        pass

    def create_truck(self)->list[Truck]:
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

