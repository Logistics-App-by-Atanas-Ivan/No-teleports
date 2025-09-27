from os import path
from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.user_roles import UserRole

#location_id

class SaveAppData(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 0)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()

        logged_in_user = self.app_data.logged_in_user
        if logged_in_user.user_role!= UserRole.MANAGER:
            raise ValueError(f'Current user role {logged_in_user.user_role} - only managers can save the application data')

        data='to be implemented'

        cwd = path.dirname(__file__)
        file_path = path.join(cwd,'../data/app_state.json')
        json_file = open(file_path, mode='w')
        contents = json_file.write()

        return 'App data has been saved successfully'
    
    def _requires_login(self) -> bool:
        return True