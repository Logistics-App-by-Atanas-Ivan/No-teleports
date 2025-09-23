from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.package import Package
from models.route import Route
from datetime import datetime

#route_id *package_id

class BulkAssignById(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 2)
        super().__init__(params, app_data)


    def execute(self):
        route_id, *package_ids = self.params
        route_id = self.try_parse_int(route_id)
        package_ids = [package_id for package_id in package_ids if self.try_parse_int(package_id)]
        packages = []
        route = self.app_data.find_route(route_id)
        if not route:
            raise(f'Route with ID {route_id} does not exist!')        
        if not route.assigned_truck:
            raise ValueError(f'No truck assigned to route with ID {route_id}')
        
        for package_id in package_ids:
            package = self.app_data.find_package(package_id)
            if not package:
                raise ValueError(f'Package with ID {package_id} does not exist!')
            packages.append(package)
        
        lines = []
        for package in packages:
            if not package.start_location in route.locations:
                raise ValueError(f'Package ID {package.packpackage_id} | Start Location {package.start_location} is not on this route!')
            if not package.end_location in route.locations:
                raise ValueError(f'Package ID {package.packpackage_id} | End Location {package.end_location} is not on this route!')            
            if package.start_location == route.locations[-1]:
                raise ValueError(f'Location {package.start_location} is the end location of this route!')
            
            if self.app_data.location_eta(route, package.start_location) < datetime.now():
                raise ValueError(f'Package ID {package.packpackage_id} | Start Location\'s ETA is in the past!')
            self.app_data.assign_package(package)
            lines.append(f'Package ID {package.package_id} has been assigned to Route ID {route.route_id}!')

        return '\n'.join(lines)
    
    def _requires_login(self) -> bool:
        return True