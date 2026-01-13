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
    def departure_time(self)->datetime:
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
            if self.departure_time:
                info+= f'{loc} ({self.location_eta(loc).strftime("%Y-%m-%d %H:%M")}) -> '
            else:
                info+= f'{loc} (ETA: N/A) -> '

        return info[:-4]
    
    
    def route_report(self, func: Callable[[Package, dict[str,int]],dict[str,int]] = None )->str:
        loads_per_location={}
        for package in self._assigned_packages:
            loads_per_location = func(package, loads_per_location)

        load_at_start_location = 0

        for package in self._assigned_packages:
            if package.start_location==self.locations[0]:
                load_at_start_location+=package.weight

        headline = str(self)+'\n'+f'{self.locations[0]} - {load_at_start_location} kg'

        next_stop =''
        total_weight_delivered = '\n'+f'Total weight: {sum(package.weight for package in self._assigned_packages)} kg'

        for loc in self.locations[1:]:


            if datetime.now()+timedelta(hours=24) < self.location_eta(loc):
                next_stop = '\n'+f'Expexted current stop: {loc}' 

            headline += '\n'+f'{loc} - {loads_per_location.get(loc, 0)} kg'

        return headline + next_stop + total_weight_delivered
        

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
    


    def to_dict(self):
        return {
            'route_id' : self.route_id,
            'locations' : self.locations,
            'departure_time' : self.departure_time.isoformat() if self.departure_time else None,
            'assigned_truck' : self.assigned_truck.to_dict() if self.assigned_truck else None,
            'assigned_packages' : [package.to_dict() for package in self._assigned_packages]
        }
    
    @classmethod
    def from_dict(cls, data, city_distances):
        route = cls(
            data['route_id'],
            data['locations'],
            city_distances
        )

        departure_time = datetime.fromisoformat(data['departure_time']) if data['departure_time'] else None
        route._departure_time = departure_time

        assigned_truck = Truck.from_dict(data['assigned_truck']) if data['assigned_truck'] else None 
        route._assigned_truck= assigned_truck


        assigned_packages = [Package.from_dict(el) for el in data.get('assigned_packages', [])] if data['assigned_packages'] else []
        route._assigned_packages = assigned_packages

        return route