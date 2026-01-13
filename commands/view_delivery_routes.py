from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.user_roles import UserRole

#location_id

class ViewDeliveryRoutes(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 0)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()

        logged_in_user = self.app_data.logged_in_user
        if logged_in_user.user_role!= UserRole.MANAGER:
            raise ValueError(f'Current user role {logged_in_user.user_role} - only managers can view all active delivery routes')

        active_routes = self.app_data.find_active_routes()
        if not active_routes:
            raise ValueError('There are no active routes.')

        lines = []
        for route in active_routes:
            lines.append(route.route_report(self.app_data.loads_per_location))
            

        return '\n'.join(lines)
    
    def _requires_login(self) -> bool:
        return True