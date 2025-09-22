from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.package import Package
from models.route import Route
from datetime import datetime

#route_id location

class BulkAssignAtLocation(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 2)
        super().__init__(params, app_data)


    def execute(self):
        route_id = self.try_parse_int(self.params[0])
        location = self.location_exists(self.params[1])

        route = self.app_data.find_route(route_id)
        if not route:
            raise(f'Route with ID {route_id} does not exist!')
        
        if not location in route.locations:
            raise ValueError(f'Location {location} is not on this route!')
        if location == route.locations[-1]:
            raise ValueError(f'Location {location} is the end location of this route!')
        if not route.assigned_truck:
            raise ValueError(f'No truck assigned to route with ID {route_id}')
        if route.location_eta(location) < datetime.now():
            raise ValueError(f'Location\'s ETA is in the past!')
                        
        bulk_assigned_packages = route.bulk_assign_at_location(location, self._app_data.packages, self.app_data.loads_per_location)

        lines = [f'Location: {loc} - Loaded weight: {kg} kg' for loc, kg in bulk_assigned_packages.items()]
        return '\n'.join(lines)