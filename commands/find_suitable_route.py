from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.status import Status

#findsuitableroute package_id

class FindSuitableRoute(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        package_id = self.try_parse_int(self.params[0])
    
        package = self.app_data.find_package(package_id)

        
        if not package.status== Status.UNASSIGNED:
            raise ValueError(
                f'Invalid package status. Expected status: {Status.UNASSIGNED} | Received status: {package.status}')
        
        available_routes = self.app_data.find_existing_route(package)

        if not available_routes:
            return f'No available routes for package with ID {package.package_id}'

        return f'Available routes for package {package.package_id}:\n' + '\n'.join(str(route) for route in available_routes)
    
    def _requires_login(self) -> bool:
        return True