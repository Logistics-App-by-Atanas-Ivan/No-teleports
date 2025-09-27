from core.application_data import ApplicationData
from commands.base.base import BaseCommand

#findtruck route_id

class FindTruck(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        super().execute()
        route_id = self.try_parse_int(self.params[0])
    
        route = self.app_data.find_route(route_id)
        if not route:
            raise ValueError(f'Route with ID {route_id} does not exist!')
        if route.assigned_truck:
            raise ValueError(f'A truck has already been assigned to Route with ID {route_id}!')
        
        suitable_truck = self.app_data.find_truck(route)

        return f'Truck with ID {suitable_truck.truck_id} | Brand: {suitable_truck.truck_brand} | Capacity: {suitable_truck.truck_capacity} kg | Range: {suitable_truck.truck_range} km is available from {suitable_truck.available_from.strftime("%Y-%m-%d %H:%M")}!'
    
    def _requires_login(self) -> bool:
        return True
    
    