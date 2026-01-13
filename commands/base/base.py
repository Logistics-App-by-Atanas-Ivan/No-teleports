from core.application_data import ApplicationData
from commands.validation_helpers import ValidationHelpers


class BaseCommand(ValidationHelpers):

    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    @property
    def params(self):
        return tuple(self._params)

    @property
    def app_data(self)->ApplicationData:
        return self._app_data

    def execute(self):
        if self._requires_login() and not self._app_data.has_logged_in_user:
            raise ValueError('You are not logged in! Please login first!')
        
    
        return ""
    
    def _requires_login(self) -> bool:
        raise NotImplementedError('Override in derived class')
    
    
    def _throw_if_user_logged_in(self):
        if self._app_data.has_logged_in_user:
            logged_user = self._app_data.logged_in_user
            raise ValueError(
                f'User with email {logged_user.email} logged in! Please log out first!')
    

    