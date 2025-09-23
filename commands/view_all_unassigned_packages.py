from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.user_roles import UserRole

#location_id

class ViewAllUnassignedPackages(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 0)
        super().__init__(params, app_data)

    def execute(self):

        logged_in_user = self.app_data.logged_in_user
        if logged_in_user.user_role== UserRole.REGULAR:
            raise ValueError(f'Current user role {logged_in_user.user_role} - only managers and supervisors can view all unassigned packages')

        unassigned_packages= self.app_data.view_all_unassigned_packages()

        return '\n'.join([str(package) for package in unassigned_packages])
    
    def _requires_login(self) -> bool:
        return True