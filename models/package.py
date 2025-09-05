from datetime import datetime

class Package:
    def __init__(self, package_id, start_location, end_location, weight, user):
        self._package_id = package_id
        self._start_location = start_location
        self._end_location= end_location
        self._weight = weight 
        self._user = user 
        self._package_eta = None

    @property
    def package_id(self):
        return self._package_id 

    @property
    def status(self):
        if self.package_eta is None: 
            return 'unassigned'
        if self.package_eta>datetime.now():
            return 'assigned'
        return 'delivered'

    @property
    def weight(self):
        return self._weight
    
    @property
    def package_eta(self):
        return self._package_eta
    
    @package_eta.setter
    def package_eta(self, value):
        if self.status=='unassigned':
            self._package_eta=value
        else:
            raise ValueError(f'ETA for package with ID {self.package_id} has already been set.')

    @property
    def info(self):
        if self.status=='unassigned':
            return f"Package with ID {self.package_id} hasn't been dispatched yet! | Location - {self._start_location}"
        if self.status=='assigned':
            return f"Package with ID {self.package_id} is on its way to {self._end_location}! | ETA - {self.package_eta}"
        
        return f'Package with ID {self.package_id} has been delivered to {self._end_location} on date_stamp?!?!?! '






    
        


        
     