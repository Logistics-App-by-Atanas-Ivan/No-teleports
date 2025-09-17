class User:
    def __init__(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._first_name
    
    @property
    def email(self):
        return self._email