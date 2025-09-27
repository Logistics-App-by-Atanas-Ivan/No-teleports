from enum import Enum


class Status(Enum):
    
    UNASSIGNED = 'Unassigned'
    ASSIGNED = 'Assigned'
    DELIVERED = 'Delivered'

    AVAILABLE = 'Available'
    UNAVAILABLE = 'Unavailable'