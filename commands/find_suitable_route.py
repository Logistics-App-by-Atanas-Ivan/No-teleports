from core.application_data import ApplicationData
from commands.base.base import BaseCommand
from models.constants.status import Status

#findsuitableroute package_id

class FindSuitableRoute(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self.validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        package_id = self.try_parse_int(self.params[0])
    
        package = self.app_data.find_package(package_id)

        if package is None:
            raise ValueError(f'Package with ID {package_id} does not exist!')
        
        if not package.status== Status.UNASSIGNED:
            raise ValueError(
                f'Invalid package status. Expected status: {Status.UNASSIGNED} | Received status: {package.status}')
        
        available_routes = self.app_data.find_existing_route(package)

        if not available_routes:
            return f'No available routes for package with ID {package.package_id}'

        return f'Available routes for package {package.package_id}:\n' + '\n'.join(route.info for route in available_routes)


# class CreateProductCommand:

#     def __init__(self, params, app_data: ApplicationData):
#         validate_params_count(params, 4)
#         self._params = params
#         self._app_data = app_data

#     def execute(self):
#         name, brand, price_str, gender_str = self._params
#         price = try_parse_float(price_str)
#         gender = Gender.from_string(gender_str)

#         if self._app_data.product_exists(name):
#             raise ValueError(
#                 f'Product with name {name} already exists!')

#         self._app_data.create_product(name, brand, price, gender)

#         return f'Product with name {name} was created!'