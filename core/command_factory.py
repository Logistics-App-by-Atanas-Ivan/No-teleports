from core.models_factory import ModelsFactory
from commands.create_package import CreatePackage
from commands.find_suitable_route import FindSuitableRoute
from commands.add_package import AddPackage
from commands.create_route import CreateRoute
from commands.assign_truck import AssignTruck
from commands.find_truck import FindTruck
from commands.view_unassigned_packages import ViewUnassignedPackages
from commands.bulk_assign_at_location import BulkAssignAtLocation
from commands.bulk_assign_by_id import BulkAssignById
from commands.find_customer import FindCustomer
from commands.create_customer import CreateCustomer


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
            return CreateRoute(params, self._app_data, self._models_factory)
        
        if cmd.lower() == "assigntruck":
            return AssignTruck(params, self._app_data)        

        if cmd.lower() == "findsuitableroute":
            return FindSuitableRoute(params, self._app_data)

        if cmd.lower() == "findtruck":
            return FindTruck(params, self._app_data)

        if cmd.lower() == "viewunassignedpackages":
            return ViewUnassignedPackages(params, self._app_data)
        
        if cmd.lower() == "bulkassignatlocation":
            return BulkAssignAtLocation(params, self._app_data)
        
        if cmd.lower() == "findcustomer":
            return FindCustomer(params, self._app_data)        

        if cmd.lower() == "createcustomer":
            return CreateCustomer(params, self._app_data, self._models_factory)

        # if cmd.lower() == "bulkassignbyid":
        #     return BulkAssignById(params, self._app_data)                     

        # if cmd.lower() == "totalprice":
        #     return TotalPriceCommand(self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')
    


