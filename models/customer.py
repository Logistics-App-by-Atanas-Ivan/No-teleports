from models.user import User

class Customer(User):
    
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        pass

    def send_email(self): 
        pass #return as a string all the content that will potentially be sent to the customer, simulating what could be sent