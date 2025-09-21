from datetime import datetime
from models.package import Package
from models.truck import Truck
from models.city_distances import CityDistances

class Route:
    def __init__(self, id, locations):
        self._route_id = id
        self._locations= locations #','.split(locations) #[location for location in locations]
        self._departure_time= None
        self._assigned_truck: Truck= None
        self._assigned_packages: list[Package] = []

    @property
    def route_id(self):
        return self._route_id

    @property
    def locations(self):
        return tuple(self._locations)
    
    @property
    def departure_time(self):
        return self._departure_time
    
    @departure_time.setter
    def departure_time(self, value):
        if self.departure_time is None:
            self._departure_time=value
        else:
            raise ValueError(f'The departure time of this route has already been set.')
        
    @property
    def assigned_truck(self):
        return self._assigned_truck
    
    @assigned_truck.setter
    def assigned_truck(self, truck: Truck):
        if self.assigned_truck is None:
            self._assigned_truck=truck
            self.departure_time = truck.available_from  #Open 1: Set this to be the next day. 
                                                        #Open 2: Should this be departure_date / departure_time / departure_date_and_time ?
        else:
            raise ValueError(f'A truck for this route has already been assigned.')


    # def location_eta(self, location)->datetime:
    #     if location == self._locations[0]:
    #         return self.departure_time
    #     pass # calculates ETA for a given location 
    

    @property
    def info(self):
        pass

    def free_capacity_at_location(self, package : Package):
        loaded_weight = 0

        for location in self._locations:            
            for assigned_package in self._assigned_packages:
                if assigned_package.start_location == location:
                    loaded_weight += assigned_package.weight
                if assigned_package.end_location == location:
                    loaded_weight -= assigned_package.weight
            if location == package.start_location:
                break
        if loaded_weight + package.weight <= self._assigned_truck.truck_capacity:
            return True
        
    def assign_package(self, package: Package):
        self._assigned_packages.append(package)