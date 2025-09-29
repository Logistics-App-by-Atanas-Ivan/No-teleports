from core.models_factory import ModelsFactory
from commands.create_package import CreatePackage
from commands.find_suitable_route import FindSuitableRoute
from commands.add_package import AddPackage
from commands.create_route import CreateRoute
from commands.assign_truck import AssignTruck
from commands.find_truck import FindTruck
from commands.view_unassigned_packages_at_location import ViewUnassignedPackagesAtLocation
from commands.bulk_assign_at_location import BulkAssignAtLocation
from commands.find_customer import FindCustomer
from commands.create_customer import CreateCustomer
from commands.login import Login
from commands.logout import Logout
from commands.create_user import CreateUser
from commands.view_all_unassigned_packages import ViewAllUnassignedPackages
from commands.find_package import FindPackage
from commands.view_delivery_routes import ViewDeliveryRoutes
from commands.save_app_data import SaveAppData
from models.city_distances import CityDistances
from commands.bulk_assign_by_id import BulkAssignById

class CommandFactory:
    def __init__(self, data, city_distances:CityDistances):
        self._app_data = data
        self._models_factory = ModelsFactory(city_distances)

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

        if cmd.lower() == "viewunassignedpackagesatlocation":
            return ViewUnassignedPackagesAtLocation(params, self._app_data)
        
        if cmd.lower() == "bulkassignatlocation":
            return BulkAssignAtLocation(params, self._app_data)
        
        if cmd.lower() == "findcustomer":
            return FindCustomer(params, self._app_data)        

        if cmd.lower() == "createcustomer":
            return CreateCustomer(params, self._app_data, self._models_factory)
        
        if cmd.lower() == 'login':
            return Login(params, self._app_data)
        
        if cmd.lower() == 'logout':
            return Logout(params, self._app_data)
        
        if cmd.lower() == 'createuser':
            return CreateUser(params, self._app_data)
        
        if cmd.lower() == 'viewallunassignedpackages':
            return ViewAllUnassignedPackages(params, self._app_data)
        
        if cmd.lower() == 'findpackage':
            return FindPackage(params, self._app_data)
        
        if cmd.lower() == 'viewdeliveryroutes':
            return ViewDeliveryRoutes(params, self._app_data)
        
        if cmd.lower() == 'saveappdata':
            return SaveAppData(params, self._app_data)
        
        # if cmd.lower() == "bulkassignbyid":
        #     return BulkAssignById(params, self._app_data)                     

        raise ValueError(f'Invalid command name: {cmd}!')
    


