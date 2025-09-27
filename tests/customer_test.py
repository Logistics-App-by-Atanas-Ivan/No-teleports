import unittest
import tests.test_data as td
from models.customer import Customer

class Customer_Should(unittest.TestCase):
    def test_init_setProperties(self):
        # Arrange & Act

        customer = Customer(td.VALID_FIRSTNAME, td.VALID_LASTNAME, td.VALID_EMAIL)

        # Assert
        self.assertEqual(customer.first_name, td.VALID_FIRSTNAME)
        self.assertEqual(customer.last_name, td.VALID_LASTNAME)
        self.assertEqual(customer.email, td.VALID_EMAIL)

    def test_init_raiseError_first_name_too_short(self):
        with self.assertRaises(ValueError):
            customer = Customer('c', td.VALID_LASTNAME, td.VALID_EMAIL)

    def test_init_raiseError_first_name_too_long(self):
        with self.assertRaises(ValueError):
            customer = Customer('c' * 21, td.VALID_LASTNAME, td.VALID_EMAIL)

    def test_init_raiseError_last_name_too_short(self):
        with self.assertRaises(ValueError):
            customer = Customer(td.VALID_FIRSTNAME, 'c', td.VALID_EMAIL)

    def test_init_raiseError_last_name_too_long(self):
        with self.assertRaises(ValueError):
            customer = Customer(td.VALID_FIRSTNAME, 'c' * 21, td.VALID_EMAIL)

    def test_init_raiseError_email_too_short(self):
        with self.assertRaises(ValueError):
            customer = Customer(td.VALID_FIRSTNAME, td.VALID_LASTNAME, 'test@')

    def test_init_raiseError_email_too_long(self):
        #Arrange
        email = 't' * 311 + '@test.test'
        with self.assertRaises(ValueError):
            customer = Customer(td.VALID_FIRSTNAME, td.VALID_LASTNAME, email)

    def test_init_raiseError_email_local_part_too_short(self):
        with self.assertRaises(ValueError):
            customer = Customer(td.VALID_FIRSTNAME, td.VALID_LASTNAME, '@test.test')

    def test_init_raiseError_email_domain_part_too_short(self):
        with self.assertRaises(ValueError):
            customer = Customer(td.VALID_FIRSTNAME, td.VALID_LASTNAME, 'test123@')

    def test_init_raiseError_email_missing_at(self):
        with self.assertRaises(ValueError):
            customer = Customer(td.VALID_FIRSTNAME, td.VALID_LASTNAME, 'test123ATtest.com')