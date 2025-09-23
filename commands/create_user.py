from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.user_roles import UserRole

# email, first_name, last_name, password, role

class CreateUser(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 5)
        super().__init__(params, app_data)
        
    def execute(self):
        super().execute()
        email, first_name, last_name, password, role = self.params
        role = role.title()

        logged_in_user = self.app_data.logged_in_user
        if logged_in_user.user_role!= UserRole.MANAGER:
            raise ValueError(f'Current user role {logged_in_user.user_role} - only managers can create new users')
        
        self.app_data.create_user(email, first_name, last_name, password, role )

        return f'User with email {email} registered successfully!'
    
    def _requires_login(self) -> bool:
        return True
    



        

        

