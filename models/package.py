from datetime import datetime, timedelta, time
from models.constants.status import Status

class Package:
    def __init__(self, package_id, start_location, end_location, weight, customer):
        self._package_id = package_id
        self._start_location = start_location
        self._end_location= end_location
        self._weight = weight 
        self._customer = customer 
        self._package_eta = None

    @property
    def package_id(self):
        return self._package_id 

    @property
    def status(self):
        
        if self.package_eta is None: 
            return Status.UNASSIGNED
        if self.package_eta>datetime.now():
            return Status.ASSIGNED
        return Status.DELIVERED

    @property
    def weight(self):
        return self._weight
    
    @property
    def package_eta(self)->datetime:
        return self._package_eta
    
    @package_eta.setter
    def package_eta(self, value):
        if self.status==Status.UNASSIGNED:
            self._package_eta=value
        else:
            raise ValueError(f'ETA for package with ID {self.package_id} has already been set.')
        
    @property
    def start_location(self):
        return self._start_location
    @property
    def end_location(self):
        return self._end_location

    @property
    def info(self):
        if self.status==Status.UNASSIGNED:
            return f"Package with ID {self.package_id} hasn't been dispatched yet! | Location - {self._start_location}"
        if self.status==Status.ASSIGNED:
            return f"Package with ID {self.package_id} is on its way to {self._end_location}! | ETA - {self.package_eta}"
        
        return f'Package with ID {self.package_id} has been delivered to {self._end_location} on {self.package_eta}'

    def __str__(self):
        if self.package_eta:

            return f'ID: {self.package_id} | Start Location: {self.start_location} | End Location: {self.end_location} | ETA: {self.package_eta.strftime("%Y-%m-%d %H:%M")}'
        
        return f'ID: {self.package_id} | Start Location: {self.start_location} | End Location: {self.end_location} | ETA: N/A'




    
        


        
     