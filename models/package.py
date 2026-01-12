from datetime import datetime, timedelta, time
from models.constants.status import Status
from models.customer import Customer

class Package:
    def __init__(self, package_id, start_location, end_location, weight, customer):
        self.package_id = package_id
        self._start_location = start_location
        self._end_location= end_location
        self.weight = weight 
        self._customer: Customer = customer 
        self._package_eta = None

    @property
    def package_id(self):
        return self._package_id
    @package_id.setter
    def package_id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._package_id = value

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
    @weight.setter
    def weight(self, value):
        if value<=0:
            raise ValueError('Package weight cannot be zero or negative')
        self._weight = value
        
    
    @property
    def package_eta(self)->datetime:
        return self._package_eta
    
    @package_eta.setter
    def package_eta(self, value: datetime):
        if self._package_eta is not None:
            raise ValueError(f'ETA for package with ID {self.package_id} has already been set.')
        if not isinstance(value, datetime):
            raise ValueError("ETA must be a datetime object")
        self._package_eta = value
        
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



    def to_dict(self):
        return {
            'package_id' : self.package_id,
            'start_location' : self.start_location,
            'end_location' : self.end_location,
            'customer' : self._customer.to_dict(),
            'weight' : self.weight,
            'package_eta' : self.package_eta.isoformat() if self.package_eta else None,
        }
    
    @classmethod
    def from_dict(cls, data):
        customer = Customer.from_dict(data['customer'])
        package = cls(
            data['package_id'],
            data['start_location'],
            data['end_location'],
            data['weight'],
            customer
        )
        if data['package_eta']:
            package._package_eta = datetime.fromisoformat(data['package_eta'])

        return package
    
        


        
     