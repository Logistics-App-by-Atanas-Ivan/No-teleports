from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.package import Package
from models.route import Route

#addpackage package_id route_id

class AddPackage(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 2)
        super().__init__(params, app_data)


    def execute(self):
        package_id = self.try_parse_int(self.params[0])    
        package = self.app_data.find_package(package_id)
        if package is None:
            raise ValueError(f'Package with ID {package_id} does not exist!')
        
        route_id = self.try_parse_int(self.params[1])

        routes = self.app_data.find_existing_route(package)
        if not routes:
            return f'No available routes for package with ID {package.package_id}'
        
        for existing_route in routes:
            if existing_route.route_id == route_id:
                if not existing_route.assigned_truck:
                    raise ValueError(f'Route with ID {existing_route.route_id} does not have an assigned truck!')
                #self.app_data.assign_package(package,existing_route)
                existing_route.assign_package(package)
                break
        else:
            return f'Package with ID {package_id} cannot be sent via route {route_id}!'

        return f'Package with ID {package.package_id} was added to route {route_id}!'