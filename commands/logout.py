from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.user_roles import UserRole

# email,password
class Logout(BaseCommand):
    def __init__(self, params, app_data):
        self.validate_params_count(params, 0)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        user = self.app_data.logged_in_user

        self._app_data.logout()

        return f'User {user.first_name} {user.last_name} logged out!'
    
    def _requires_login(self) -> bool:
        return True