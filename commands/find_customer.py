from core.application_data import ApplicationData
from commands.base.base import BaseCommand

#findclient email

class FindCustomer(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        super().execute()
        email = self.params[0] #Open: Add email validations
        
        customer = self.app_data.find_customer(email)
        if not customer:
            raise ValueError(f'Customer with email {email} does not exist!')
        
        return f'Customer - Email {email} | First Name: {customer.first_name} | Last Name: {customer.last_name}.' #Extend with creation date & time
    
    def _requires_login(self) -> bool:
        return True