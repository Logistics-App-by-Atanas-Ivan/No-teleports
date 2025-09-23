from core.application_data import ApplicationData
from commands.base.base import BaseCommand

#FindPackage id

class FindPackage(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        package_id = self.params[0] 

        package = self.app_data.find_package(int(package_id))

        
        return str(package)
    
    def _requires_login(self) -> bool:
        return True