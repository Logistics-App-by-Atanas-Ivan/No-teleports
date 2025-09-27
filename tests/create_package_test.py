import unittest
from unittest.mock import Mock
from commands.create_package import CreatePackage
from models.package import Package
from core.application_data import ApplicationData

#createpackage start_city end_city weight email 

class CreatePackage_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = Mock()
        self.models_factory = Mock()


    def test_params_property(self):
        params = ['Sydney', 'Melbourne', '45', 'atanas@telerikacademy.com']
        cmd = CreatePackage(params, self.app_data, self.models_factory)
        self.assertEqual(tuple(params),cmd.params)

    def test_execute_raiseError_invalid_start_location(self): 
        params = ['Syd', 'Melbourne', '45', 'atanas@telerikacademy.com']
        cmd = CreatePackage(params, self.app_data, self.models_factory)

        with self.assertRaises(ValueError) as msg:
            cmd.execute()
        self.assertIn('Please enter a valid start location.', str(msg.exception))

    def test_execute_raiseError_invalid_end_location(self): 
        params = ['Sydney', 'Melbo', '45', 'atanas@telerikacademy.com']
        cmd = CreatePackage(params, self.app_data, self.models_factory)

        with self.assertRaises(ValueError) as msg:
            cmd.execute()
        self.assertIn('Please enter a valid end location.', str(msg.exception))

    def test_execute_raiseError_invalid_weight(self): 
        params = ['Sydney', 'Melbourne', 'fourty', 'atanas@telerikacademy.com']
        cmd = CreatePackage(params, self.app_data, self.models_factory)

        with self.assertRaises(ValueError) as msg:
            cmd.execute()
        self.assertIn('Invalid value. Should be a number.',str(msg.exception))

    def test_execute_raiseError_no_customer(self): 
        params = ['Sydney', 'Melbourne', '45', 'atanas@telerikacademy.com']
        self.app_data.find_customer.return_value = None
        cmd = CreatePackage(params, self.app_data, self.models_factory)

        with self.assertRaises(ValueError) as msg:
            cmd.execute()
        self.assertIn('Customer with email atanas@telerikacademy.com not found!', str(msg.exception))

    def test_requires_login(self):
        params = ['Sydney', 'Melbourne', '45', 'atanas@telerikacademy.com']
        self.app_data.has_logged_in_user = False
        cmd = CreatePackage(params, self.app_data, self.models_factory)

        with self.assertRaises(ValueError) as cm:
            cmd.execute()

        self.assertIn('You are not logged in! Please login first!', str(cm.exception))

    def test_execute_returns_success_message(self):
        params = ['Sydney', 'Melbourne', '45', 'atanas@telerikacademy.com']
        customer = object()
        package = Mock()
        
        package.package_id = 1

        self.app_data.find_customer.return_value = customer
        self.models_factory.create_package.return_value = package

        cmd = CreatePackage(params, self.app_data, self.models_factory)
  

    
        self.assertEqual('Package with ID 1 was created!', cmd.execute())










