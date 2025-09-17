from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.base.base import BaseCommand

#createpackage start_city end_city weight email 

class CreatePackage(BaseCommand):

    def __init__(self, params, app_data: ApplicationData, models_factory: ModelsFactory):
        self.validate_params_count(params, 4)
        super().__init__(params, app_data)
        self._models_factory = models_factory


    def execute(self):
        start_location, end_location, weight, email = self.params
        start_location = self.location_exists(start_location)
        end_location = self.location_exists(end_location, False)
        weight = self.try_parse_float(weight)
        user = self.app_data.find_user(email)
        if not user:
            raise ValueError(f'User with email {email} not found!')
        
        package = self._models_factory.create_package(start_location, end_location, weight, user)

        self.app_data.add_package(package)

        return f'Package with ID {package.id} was created!'