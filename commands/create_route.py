from core.application_data import ApplicationData
from commands.base.base import BaseCommand

#createroute locations

class CreateRoute(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        route_locations = self.params[0]
        for location in route_locations:
            self.location_exists(location)

        route = self
        
        # start_location, end_location, weight, email = self.params
        # start_location = self.location_exists(start_location)
        # end_location = self.location_exists(end_location, False)
        # weight = self.try_parse_float(weight)
        # user = self.app_data.user_exists(email) # implement later
        
        # package = self._models_factory.create_package(start_location, end_location, weight, user)

        # self.app_data.add_package(package)

        # return f'Package with ID {package.id} was created!'