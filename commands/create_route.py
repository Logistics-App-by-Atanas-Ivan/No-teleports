from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.base.base import BaseCommand

#createroute locations

class CreateRoute(BaseCommand):

    def __init__(self, params, app_data: ApplicationData, models_factory: ModelsFactory):
        # self.validate_params_count(params, 1)
        # params= [el for el in params]
        for i in range(len(params)-1):
            if params[i].title()=='Alice' and params[i+1].title()=='Springs':
                params[i]='Alice Springs'
                params.pop(i+1)
           
        if len(params)<2:
            raise ValueError(f'Invalid number of arguments. Expected: minimum two; received: {len(params)}.')
        super().__init__(params, app_data)
        self._models_factory = models_factory

    def execute(self):
        super().execute()
        route_locations = self._params

        for idx in range(len(route_locations)):
            adjusted_loc = self.location_exists(route_locations[idx])
            route_locations[idx] = adjusted_loc            

    
        route = self._models_factory.create_route(route_locations)
        self.app_data.add_route(route)

        return f'Route with ID {route.route_id} was created!'
    
    def _requires_login(self) -> bool:
        return True