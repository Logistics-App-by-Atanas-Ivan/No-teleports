from datetime import datetime 
from models.constants.status import Status

class Truck:
    def __init__(self, id: int, brand: str, capacity: int, range: int):
        self._truck_id = id
        self._truck_brand = brand
        self._truck_capacity = capacity
        self._truck_range = range
        self._avaialble_from = datetime.now()
    
    @property
    def truck_id(self):
        return self._truck_id
    
    @property
    def truck_brand(self):
        return self._truck_brand
    
    @property
    def truck_capacity(self):
        return self._truck_capacity
    
    @property
    def truck_range(self):
        return self._truck_range
    
    @property
    def available_from(self) -> datetime:
        return self._avaialble_from
    
    @available_from.setter
    def available_from(self, date):
        if date<self.available_from:
            raise ValueError('The truck is unavailable for the date you ahve entered.')
        self._available_from = date

    @property
    def truck_status(self):
        if self.available_from>datetime.now():
            return Status.UNAVAILABLE
        return Status.AVAILABLE