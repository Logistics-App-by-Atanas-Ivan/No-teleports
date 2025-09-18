from core.application_data import ApplicationData
from commands.base.base import BaseCommand

#assigntruck truck_id route_id

class AssignTruck(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 2)
        super().__init__(params, app_data)


    def execute(self):
        truck_id, route_id = self.params
        truck_id = self.try_parse_int(truck_id)
        route_id = self.try_parse_int(route_id)

        truck = self.app_data.find_truck(truck_id)
        if not truck:
            raise ValueError(f'Truck with ID {truck_id} was not found!')
        
        route = self.app_data.find_route(route_id)
        if not route:
            raise ValueError(f'Route with ID {route_id} was not found!')
        
        self.app_data.assign_truck(route, truck)

        return f'Truck with ID {truck_id} was assigned to Route with ID {route_id}!'