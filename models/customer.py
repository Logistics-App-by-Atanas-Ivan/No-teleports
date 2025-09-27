from validators.fields import FieldValidators

class Customer:
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value: str):
        FieldValidators.validate_first_name(value)
        self._first_name = value            


    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str):
        FieldValidators.validate_last_name(value)
        self._last_name = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value: str):
        FieldValidators.validate_email(value)
        self._email = value