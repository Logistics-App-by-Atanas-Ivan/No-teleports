import unittest
from unittest.mock import Mock
from models.package import Package
from models.constants.status import Status
from datetime import datetime, timedelta, time

class Package_Should(unittest.TestCase):
    def test_constructor_initializes_attributes_correctly(self):
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)

        self.assertEqual(1, package.package_id)
        self.assertEqual(40.0, package.weight)
        self.assertIsNone(package.package_eta)
        self.assertEqual(Status.UNASSIGNED, package.status)

    def test_init_raiseError_invalidIds(self):
        customer = Mock()
        invalid_ids = ['1',1.0,None]

        for invalid_id in invalid_ids:
            with self.subTest(invalid_input = invalid_id):
                with self.assertRaises(ValueError):
                    Package(invalid_id, "Melbourne", "Sydney", 40.0, customer)


    def test_init_raiseError_invalidWeight(self):
        customer = Mock()
        invalid_values= [0, -1]

        for invalid_input in invalid_values:
            with self.subTest(invalid_value = invalid_input):
                with self.assertRaises(ValueError):
                    Package(1, "Melbourne", "Sydney", invalid_input, customer)

    
    def test_eta_setter(self):
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)

        eta = datetime.now() + timedelta(hours=24)
        package.package_eta = eta

        self.assertEqual(eta, package.package_eta)


    def test_eta_setter_raiseError_no_datetime_object(self):       
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)

        eta = 'invalid input'
        
        with self.assertRaises(ValueError):
            package.package_eta=eta

    
    def test_eta_setter_raiseError_eta_already_set(self):       
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)

        package.package_eta = datetime.now()
        
        with self.assertRaises(ValueError):
            package.package_eta=datetime.now() + timedelta(hours=24)


    def test_status_getter_unassigned_assigned(self):       
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)

        self.assertEqual(Status.UNASSIGNED, package.status)

        package.package_eta = datetime.now() + timedelta(hours=24)
        self.assertEqual(Status.ASSIGNED, package.status)


    def test_status_getter_delivered(self):       
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)

        package.package_eta = datetime.now() - timedelta(hours=24)

        self.assertEqual(Status.DELIVERED, package.status)


    def test_str_method_returns_correctly_no_eta(self):       
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)

        self.assertEqual(f'ID: 1 | Start Location: Melbourne | End Location: Sydney | ETA: N/A', str(package))


    def test_str_method_returns_correctly_eta(self):       
        customer = Mock()
        package = Package(1, "Melbourne", "Sydney", 40.0, customer)
        eta= datetime.now()

        package.package_eta=eta

        self.assertEqual(f'ID: 1 | Start Location: Melbourne | End Location: Sydney | ETA: {eta.strftime("%Y-%m-%d %H:%M")}', str(package))





        


    



    
        
        
