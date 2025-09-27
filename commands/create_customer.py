from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.base.base import BaseCommand

#createcustomer first_name last_name email

class CreateCustomer(BaseCommand):

    def __init__(self, params, app_data: ApplicationData, models_factory: ModelsFactory):
        self.validate_params_count(params, 3)
        super().__init__(params, app_data)
        self._models_factory = models_factory

    def execute(self):
        super().execute()
        first_name, last_name, email = self.params #validations
        customer = self._models_factory.create_customer(first_name, last_name, email)
        self.app_data.add_customer(customer)

        return f'Customer with Email {email} was created!'
    
    def _requires_login(self) -> bool:
        return True