from core.application_data import ApplicationData
from commands.base.base import BaseCommand

#location_id

class ViewUnassignedPackages(BaseCommand):
    pass

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        location = self.location_exists(self.params[0])

        unassigned_packages = self.app_data.view_unassigned_packages(location)
        lines = [f'Location: {loc} - Total weight: {kg} kg' for loc, kg in unassigned_packages.items()]
        return '\n'.join(lines)