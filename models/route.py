from datetime import datetime

class Route:
    def __init__(self,*args):
        self._locations=[]
        self._departure_time= None
        self._assigned_truck = None

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
    def assigned_truck(self, value):
        if self.assigned_truck is None:
            self._assigned_truck=value
        else:
            raise ValueError(f'A truck for this route has already been assigned.')


    def location_eta(self, location)->datetime:
        if location == self._locations[0]:
            return self.departure_time
        pass # calculates ETA for a given location 
    
    @property
    def info(self):
        pass