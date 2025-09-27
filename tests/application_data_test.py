import unittest

from core.application_data import ApplicationData
from models.constants.user_roles import UserRole
from models.truck import Truck

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
        pass       


class CreateUser(unittest.TestCase):
    pass

class FindUser_Should(unittest.TestCase):
    pass

class AddCustomer_Should(unittest.TestCase):
    pass

class FindCustomer_Should(unittest.TestCase):
    pass

class AddPackage_Should(unittest.TestCase):
    pass

class FindPackage_Should(unittest.TestCase):
    pass

class ViewAllUnassignedPackages_Should(unittest.TestCase):
    pass

class ViewUnassignedPackagesAtLocation_Should(unittest.TestCase):
    pass

class LoadsPerLocationShould_Should(unittest.TestCase):
    pass

class AddRoute_Should(unittest.TestCase):
    pass

class FindRoute_Should(unittest.TestCase):
    pass

class FindExistingRoute_Should(unittest.TestCase):
    pass

class FindActiveRoutes_Should(unittest.TestCase):
    pass

class FindTruck_Should(unittest.TestCase):
    pass