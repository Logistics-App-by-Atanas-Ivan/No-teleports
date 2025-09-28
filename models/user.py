from models.constants.user_roles import UserRole

class User:
    def __init__(self, email, first_name, last_name, password, role):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._user_role = role
        self.password = password

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @property
    def user_role(self):
        return self._user_role
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,value : str):
        if not 5<=len(value)<=30:
            raise ValueError(f'Password must be between 5 and 30 characters long!')
        
        for symbol in value:
            if not symbol.isalpha() and not symbol.isdigit() and symbol!='@' and symbol!= '*' and symbol!= '-' and symbol!= '_':
                raise ValueError ('Password contains invalid symbols!')
        self._password = value 

