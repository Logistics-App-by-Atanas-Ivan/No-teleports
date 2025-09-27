from core.application_data import ApplicationData
from commands.base.base import BaseCommand

#location_id

class ViewUnassignedPackagesAtLocation(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        location = self.location_exists(self.params[0])

        unassigned_packages_at_location = self.app_data.view_unassigned_packages_at_location(location)

        lines = [f'Location: {loc} - Total weight: {kg} kg' for loc, kg in unassigned_packages_at_location.items()]

        return '\n'.join(lines)
    
    def _requires_login(self) -> bool:
        return True