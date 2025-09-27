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
        super().execute()
    
        start_location, end_location, weight, email = self.params
        start_location = self.location_exists(start_location)
        end_location = self.location_exists(end_location, False)
        weight = self.try_parse_float(weight)
        customer = self.app_data.find_customer(email)
        if not customer:
            raise ValueError(f'Customer with email {email} not found!')
        
        package = self._models_factory.create_package(start_location, end_location, weight, customer)

        self.app_data.add_package(package)

        return f'Package with ID {package.package_id} was created!'
    
    def _requires_login(self) -> bool:
        return True