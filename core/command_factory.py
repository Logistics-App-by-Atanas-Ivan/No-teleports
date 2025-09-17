from core.models_factory import ModelsFactory
from commands.create_package import CreatePackage
from commands.find_suitable_route import FindSuitableRoute
from commands.add_package import AddPackage
from commands.create_route import CreateRoute
from commands.assign_truck import AssignTruck


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

        if cmd.lower() == "addpackage":
            return AddPackage(params, self._app_data)

        if cmd.lower() == "createroute":
            return CreateRoute(params, self._app_data)
        
        if cmd.lower() == "assign_truck":
            return AssignTruck(params, self._app_data)        


        # if cmd.lower() == "totalprice":
        #     return TotalPriceCommand(self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')
    


