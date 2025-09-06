# from commands.add_to_category import AddToCategoryCommand
# from commands.add_to_shopping_cart import AddToShoppingCartCommand
# from commands.create_category import CreateCategoryCommand
# from commands.create_cream import CreateCreamCommand
# from commands.create_shampoo import CreateShampooCommand
# from commands.create_toothpaste import CreateToothpasteCommand
# from commands.remove_from_category import RemoveFromCategoryCommand
# from commands.remove_from_shopping_cart import RemoveFromShoppingCartCommand
# from commands.show_category import ShowCategoryCommand
# from commands.total_price import TotalPriceCommand
from core.models_factory import ModelsFactory
from commands.create_package import CreatePackage
from commands.find_suitable_route import FindSuitableRoute


class CommandFactory:
    def __init__(self, data):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createpackage":
            return CreatePackage(params, self._app_data,self._models_factory)
        
        if cmd.lower() == "findsuitableroute":
            return FindSuitableRoute(params, self._app_data)
        


        # if cmd.lower() == "createcream": # CREAM
        #     return CreateCreamCommand(params, self._app_data)
        # if cmd.lower() == "createshampoo":
        #     return CreateShampooCommand(params, self._app_data)
        # if cmd.lower() == "createtoothpaste":
        #     return CreateToothpasteCommand(params, self._app_data)
        # if cmd.lower() == "showcategory":
        #     return ShowCategoryCommand(params, self._app_data)
        # if cmd.lower() == "addtocategory":
        #     return AddToCategoryCommand(params, self._app_data)
        # if cmd.lower() == "removefromcategory":
        #     return RemoveFromCategoryCommand(params, self._app_data)
        # if cmd.lower() == "addtoshoppingcart":
        #     return AddToShoppingCartCommand(params, self._app_data)
        # if cmd.lower() == "removefromshoppingcart":
        #     return RemoveFromShoppingCartCommand(params, self._app_data)
        # if cmd.lower() == "totalprice":
        #     return TotalPriceCommand(self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')
    


