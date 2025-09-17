from models.employee import Employee

class Supervisor(Employee):
    
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        pass