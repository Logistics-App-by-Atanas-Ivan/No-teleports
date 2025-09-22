from datetime import datetime, timedelta, time
from models.package import Package
from models.truck import Truck
from models.city_distances import CityDistances
from models.constants.status import Status
from typing import Callable

class Route:
    def __init__(self, id, locations, city_distances: CityDistances):
        self._route_id = id
        self._locations: list[str]= locations
        self._departure_time= None
        self._assigned_truck: Truck= None
        self._assigned_packages: list[Package] = []
        self._city_distances = city_distances
    
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

        if self.assigned_truck:
            raise ValueError(f'A truck for this route has already been assigned.')
        self._assigned_truck=truck

        if truck.available_from <= datetime.combine(datetime.today().date() + timedelta(days=1), time(hour=6)): 
            self.departure_time = datetime.combine(datetime.today().date() + timedelta(days=1), time(hour=6))
        else:
            self.departure_time = datetime.combine(truck.available_from.date() + timedelta(days=1), time(hour=6))

        route_final_location = self.locations[-1]

        final_location_eta = self.location_eta(route_final_location)

        truck.available_from = final_location_eta
        

    def location_eta(self,  location)->datetime:
        if location == self._locations[0]:
            return self._departure_time
        location_eta = self.eta_calculation(location)
        return location_eta
    
    def eta_calculation(self, location) -> datetime:
        distance = self._city_distances.calculate_distance(location, self)
        travel_time_in_minutes = timedelta(minutes=(distance / 87) * 60)
        return self._departure_time + travel_time_in_minutes

    def __str__(self):
        info = f'Route ID {self.route_id} | '
        for loc in self.locations:
            info+= f'{loc} ({self.location_eta(loc).strftime("%Y-%m-%d %H:%M")}) -> '

        return info[:-4]


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
        package.package_eta = self.eta_calculation(package.end_location)
        self._assigned_packages.append(package)


    def bulk_assign_at_location(self, location: str, packages: list[Package], func_loads_per_location: Callable[[Package], dict[str, int]]) -> dict[str, int]:
        loads_per_location = {}
        next_locations = self._locations[self._locations.index(location):]
        for package in packages:
            if package.status == Status.UNASSIGNED:
                if package.start_location == location and package.end_location in next_locations:
                    if self.free_capacity_at_location(package):
                        self.assign_package(package)                      
                        loads_per_location = func_loads_per_location(package, loads_per_location)
        return loads_per_location
    


