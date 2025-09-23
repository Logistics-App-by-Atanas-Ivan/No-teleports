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

        route = self.app_data.find_route(route_id)
        if not route:
            raise ValueError(f'Route with ID {route_id} was not found!')
        
        truck = self.app_data.find_truck(route)
        if truck.truck_id != truck_id:
            raise ValueError(f'Truck with ID {truck_id} is no longer available! Please assign a different truck!')
        
        route.assigned_truck = truck

        # self.app_data.assign_truck(route, truck)

        return f'Truck with ID {truck_id} was assigned to Route with ID {route_id}!'
    
    def _requires_login(self) -> bool:
        return True