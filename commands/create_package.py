from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.base.base import BaseCommand

#createpackage start_city end_city weight email 

class CreatePackage(BaseCommand):

    def __init__(self, params, app_data: ApplicationData, models_factory: ModelsFactory):
        self.validate_params_count(params, 4)
        super().__init__(params, app_data)
        self._models_factory = models_factory


    def execute(self):
        start_location, end_location, weight, email = self.params
        start_location = self.location_exists(start_location)
        end_location = self.location_exists(end_location, False)
        weight = self.try_parse_float(weight)
        user = self.app_data.user_exists(email) # implement later
        
        package = self._models_factory.create_package(start_location, end_location, weight, user)

        self.app_data.add_package(package)

        return f'Package with ID {package.id} was created!'


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