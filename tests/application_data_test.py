import unittest
from core.application_data import ApplicationData
from models.constants.user_roles import UserRole
from models.truck import Truck
from models.city_distances import CityDistances
import tests.test_data as td
from unittest.mock import Mock
from datetime import datetime,timedelta
from models.constants.status import Status
from models.route import Route

class Initializer_Should(unittest.TestCase):
    def test_init_sets_empty_collections(self):
        # Arrange & Act
        app_data = ApplicationData()

        #Assert
        self.assertEqual(app_data.routes, ())
        self.assertEqual(app_data.packages, ())
        self.assertEqual(app_data.customers, ())
    
    def test_init_sets_empty_logged_user(self):
        # Arrange & Act
        app_data = ApplicationData()

        #Assert
        self.assertFalse(app_data.has_logged_in_user)
        with self.assertRaises(ValueError):
            logged_user = app_data.logged_in_user
    
    def test_init_sets_initial_manager(self):
        # Arrange & Act
        app_data = ApplicationData()

        #Assert
        self.assertEqual(len(app_data.users), 1)
        self.assertEqual(app_data.users[0].user_role, UserRole.MANAGER)

    def test_init_sets_fleet(self):
        # Arrange & Act
        app_data = ApplicationData()

        #Assert
        self.assertEqual(len(app_data.trucks), 40)
        for truck in app_data.trucks:
            self.assertIsInstance(truck, Truck)

    def test_init_sets_city_distances(self):
        # Arrange & Act
        app_data = ApplicationData()

        #Assert
        self.assertIsInstance(app_data._city_distances, CityDistances)


class CreateUser_Should(unittest.TestCase):
    def test_create_user_adds_correctly(self):
        # Arrange & Act
        app_data = ApplicationData()
        init_user_lenght = len(app_data.users)
        app_data.create_user(td.VALID_EMAIL, td.VALID_FIRSTNAME, 
                             td.VALID_LASTNAME, td.VALID_PASSWORD, UserRole.REGULAR)
        #Assert
        self.assertEqual(init_user_lenght + 1, len(app_data.users))
    
    def test_create_user_raises_error_when_user_exists(self):
        # Arrange
        app_data = ApplicationData()
        app_data.create_user(td.VALID_EMAIL, td.VALID_FIRSTNAME, 
                             td.VALID_LASTNAME, td.VALID_PASSWORD, UserRole.REGULAR)
        
        #Act & Assert 
        with self.assertRaises(ValueError):
            app_data.create_user(td.VALID_EMAIL, td.VALID_FIRSTNAME, 
                                td.VALID_LASTNAME, td.VALID_PASSWORD, UserRole.REGULAR)

class FindUser_Should(unittest.TestCase):
    def test_find_user_returns_correctly(self):
        # Arrange
        app_data = ApplicationData()
        new_user = app_data.create_user(td.VALID_EMAIL, td.VALID_FIRSTNAME, 
                             td.VALID_LASTNAME, td.VALID_PASSWORD, UserRole.REGULAR)

        # Act & Assert
        self.assertEqual(app_data.find_user(td.VALID_EMAIL), new_user)

    def test_find_user_raises_error_user_does_not_exist(self):
        # Arrange
        app_data = ApplicationData()
        new_user = app_data.create_user(td.VALID_EMAIL, td.VALID_FIRSTNAME, 
                             td.VALID_LASTNAME, td.VALID_PASSWORD, UserRole.REGULAR)

        # Act & Assert
        with self.assertRaises(ValueError):
            self.assertEqual(app_data.find_user('wrong_email@test.test'), new_user)

class AddCustomer_Should(unittest.TestCase):
    def test_add_custmer_adds_correctly(self):
        # Arrange
        app_data = ApplicationData()
        init_customer_lenght = len(app_data.customers)
        customer = Mock()

        #Act
        app_data.add_customer(customer)

        #Assert
        self.assertEqual(init_customer_lenght + 1, len(app_data.customers))

class FindCustomer_Should(unittest.TestCase):
    def test_find_customer_returns_correctly(self):
        # Arrange
        app_data = ApplicationData()
        customer = Mock(email = td.VALID_EMAIL)
        app_data.add_customer(customer)

        #Act & Assert
        self.assertEqual(app_data.find_customer(td.VALID_EMAIL), customer)

    def test_find_customer_raises_error_customer_does_not_exist(self):
        # Arrange
        app_data = ApplicationData()
        customer = Mock(email = td.VALID_EMAIL)
        app_data.add_customer(customer)

        #Act & Assert
        with self.assertRaises(ValueError):
            app_data.find_customer('test1@test.test')

class AddPackage_Should(unittest.TestCase):
    def test_add_package_adds_correctly(self):
        # Arrange & Act
        app_data = ApplicationData()
        init_package_lenght = len(app_data.packages)
        package = Mock()
        app_data.add_package(package)
        #Assert
        self.assertEqual(init_package_lenght + 1, len(app_data.packages))
    
    def test_add_package_raises_error_when_package_exists(self):
        # Arrange
        app_data = ApplicationData()
        package = Mock(package_id = td.VALID_PACKAGE_ID)
        app_data.add_package(package)
        
        #Act & Assert 
        with self.assertRaises(ValueError):
            app_data.add_package(package)

class FindPackage_Should(unittest.TestCase):
    def test_find_package_returns_correctly(self):
        # Arrange
        app_data = ApplicationData()
        package = Mock(package_id = td.VALID_PACKAGE_ID)
        app_data.add_package(package)

        #Act & Assert
        self.assertEqual(app_data.find_package(td.VALID_PACKAGE_ID), package)

    def test_find_package_raises_error_package_does_not_exist(self):
        # Arrange
        app_data = ApplicationData()
        package = Mock(package_id = td.VALID_PACKAGE_ID)
        app_data.add_package(package)

        #Act & Assert
        with self.assertRaises(ValueError):
            app_data.find_package(td.INVALID_PACKAGE_ID)

class ViewAllUnassignedPackages_Should(unittest.TestCase):
    def test_view_all_unassigned_packages_returns_unassigned_packages_when_present(self):
        # Arrange
        app_data = ApplicationData()
        package1 = Mock(status = Status.UNASSIGNED)

        #Act
        app_data.add_package(package1)
        unassigned_packages = app_data.view_all_unassigned_packages()
        
        #Assert
        self.assertEqual(len(unassigned_packages), 1)
    
    def test_view_all_unassigned_packages_empty_list_when_no_unassigned_packages(self):
        # Arrange
        app_data = ApplicationData()

        #Act
        unassigned_packages = app_data.view_all_unassigned_packages()
        
        #Assert
        self.assertEqual(unassigned_packages, [])

class LoadsPerLocationShould_Should(unittest.TestCase):
    def test_loads_per_location_returns_correct_dict_when_base_dict_is_empty(self):
        # Arrange
        app_data = ApplicationData()
        package = Mock(end_location = 'Perth', weight = 20)
        loads_per_location = {}

        #Act
        loads_per_location = app_data.loads_per_location(package, loads_per_location)

        #Assert
        self.assertEqual(loads_per_location['Perth'], 20)

    def test_loads_per_location_returns_correct_dict_when_base_dict_not_empty(self):
        # Arrange
        app_data = ApplicationData()
        package = Mock(end_location = 'Perth', weight = 20)
        loads_per_location = {'Perth' : 20, 'Sydney' : 30}

        #Act
        loads_per_location = app_data.loads_per_location(package, loads_per_location)

        #Assert
        self.assertEqual(loads_per_location['Perth'], 40)
        self.assertEqual(loads_per_location['Sydney'], 30)


class ViewUnassignedPackagesAtLocation_Should(unittest.TestCase):
    def test_view_unassigned_packages_at_location_returns_unassigned_packages_when_present(self):
        # Arrange
        app_data = ApplicationData()
        package1 = Mock(status = Status.UNASSIGNED, start_location = 'Sydney')

        #Act
        app_data.add_package(package1)
        unassigned_packages = app_data.view_unassigned_packages_at_location('Sydney')
        
        #Assert
        self.assertEqual(len(unassigned_packages), 1)
    
    def test_view_unassigned_packages_at_location_empty_dict_when_no_unassigned_packages(self):
        # Arrange
        app_data = ApplicationData()

        #Act
        unassigned_packages = app_data.view_unassigned_packages_at_location('Sydney')
        
        #Assert
        self.assertEqual(unassigned_packages, {})

class AddRoute_Should(unittest.TestCase):
    def test_add_route_adds_correctly(self):
        # Arrange & Act
        app_data = ApplicationData()
        init_routes_lenght = len(app_data.routes)
        route = Mock()
        app_data.add_route(route)
        #Assert
        self.assertEqual(init_routes_lenght + 1, len(app_data.routes))
    
    def test_add_route_raises_error_when_route_exists(self):
        # Arrange
        app_data = ApplicationData()
        route = Mock(route_id = td.VALID_ROUTE_ID)
        app_data.add_route(route)
        
        #Act & Assert 
        with self.assertRaises(ValueError):
            app_data.add_route(route)

class FindRoute_Should(unittest.TestCase):
    def test_find_route_returns_correctly(self):
        # Arrange
        app_data = ApplicationData()
        route = Mock(route_id = td.VALID_ROUTE_ID)
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_route(td.VALID_ROUTE_ID), route)

    def test_find_route_raises_error_route_does_not_exist(self):
        # Arrange
        app_data = ApplicationData()
        route = Mock(route_id = td.VALID_ROUTE_ID)
        app_data.add_route(route)

        #Act & Assert
        with self.assertRaises(ValueError):
            app_data.find_package(td.INVALID_ROUTE_ID)

class FindExistingRoute_Should(unittest.TestCase):
    def test_find_existing_route_returns_empty_list_when_route_has_no_truck(self):
        #Arrange
        app_data = ApplicationData()
        package = Mock(start_location = 'Sydney', end_location = 'Melbourne')
        route = Mock(assigned_truck = None)
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_existing_route(package), [])


    def test_find_existing_route_returns_empty_list_when_package_start_location_not_in_route(self):
        #Arrange
        app_data = ApplicationData()
        truck = Mock()
        package = Mock(start_location = 'Sydney', end_location = 'Melbourne')
        route = Mock(locations = ['Melbourne', 'Adelaide'])
        route.assigned_truck = truck
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_existing_route(package), [])

    def test_find_existing_route_returns_empty_list_when_package_start_location_eta_in_the_past(self):
        #Arrange
        app_data = ApplicationData()
        truck = Mock()
        package = Mock( start_location = 'Sydney', end_location = 'Melbourne')
        route = Mock(locations = ['Sydney', 'Melbourne'])
        route.assigned_truck = truck
        route.location_eta.return_value = datetime.now() - timedelta(hours=1)
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_existing_route(package), [])
    
    def test_find_existing_route_returns_empty_list_when_package_end_location_not_in_route(self):
        #Arrange
        app_data = ApplicationData()
        truck = Mock()
        package = Mock(assigned_truck = truck, start_location = 'Sydney', end_location = 'Melbourne')
        route = Mock(locations = ['Sydney', 'Adelaide'])
        route.assigned_truck = truck
        route.location_eta.return_value = datetime.now() + timedelta(hours=1)
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_existing_route(package), [])
    
    def test_find_existing_route_returns_empty_list_when_end_before_start_location(self):
        #Arrange
        app_data = ApplicationData()
        truck = Mock()
        package = Mock(assigned_truck = truck, start_location = 'Sydney', end_location = 'Melbourne')
        route = Mock(locations = ['Melbourne', 'Sydney'])
        route.assigned_truck = truck
        route.location_eta.return_value = datetime.now() + timedelta(hours=1)
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_existing_route(package), [])    

    def test_find_existing_route_returns_empty_list_when_no_free_capacity_at_load_location(self):
        #Arrange
        app_data = ApplicationData()
        truck = Mock()
        package = Mock(assigned_truck = truck, start_location = 'Sydney', end_location = 'Melbourne')
        route = Mock(locations = ['Sydney', 'Melbourne'])
        route.assigned_truck = truck
        route.location_eta.return_value = datetime.now() + timedelta(hours=1)
        route.free_capacity_at_location.return_value = None
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_existing_route(package), [])

    def test_find_existing_route_returns_valid_list_with_routes_when_all_conditions_are_met(self):
        #Arrange
        app_data = ApplicationData()
        truck = Mock()
        package = Mock(assigned_truck = truck, start_location = 'Sydney', end_location = 'Melbourne')
        route = Mock(locations = ['Sydney', 'Melbourne'])
        route.assigned_truck = truck
        route.location_eta.return_value = datetime.now() + timedelta(hours=1)
        route.free_capacity_at_location.return_value = True
        app_data.add_route(route)

        #Act & Assert
        self.assertEqual(app_data.find_existing_route(package), [route])

class FindActiveRoutes_Should(unittest.TestCase):
    pass

class FindTruck_Should(unittest.TestCase):
    pass