from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.user_roles import UserRole

# email,password
class Login(BaseCommand):
    def __init__(self, params, app_data):
        self.validate_params_count(params, 2)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        self._throw_if_user_logged_in()
        email, password = self.params

        user = self._app_data.find_user(email)
        
        if user.password != password:
            raise ValueError('Wrong username or password!')
        else:
            self._app_data.login(user)

        return f'User {user.first_name} {user.last_name} successfully logged in!'
    
    def _requires_login(self) -> bool:
        return False