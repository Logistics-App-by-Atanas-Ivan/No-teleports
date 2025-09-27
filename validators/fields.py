class FieldValidators:
    _EMAIL_LEN_MIN = 6
    _EMAIL_LEN_MAX = 320

    _FIRSTNAME_LEN_MIN = 2
    _FIRSTNAME_LEN_MAX = 20

    _LASTNAME_LEN_MIN = 2
    _LASTNAME_LEN_MAX = 20    

    @staticmethod
    def validate_email(email: str):
        if len(email) < FieldValidators._EMAIL_LEN_MIN or len(email) > FieldValidators._EMAIL_LEN_MAX:
            raise ValueError(f'Email must be between {FieldValidators._EMAIL_LEN_MIN} and {FieldValidators._EMAIL_LEN_MAX} characters long!')
        if '@' not in email:
            raise ValueError(f"Email must include '@'!")
        local_part = email.split('@')[0]
        domain_part = email.split('@')[1]
        
        if len(local_part) < 1 or len(domain_part) < 1 or len(domain_part) > 63:
            raise ValueError(f'Invalid email structure!')

    @staticmethod
    def validate_first_name(first_name: str):
        if len(first_name) < FieldValidators._FIRSTNAME_LEN_MIN or len(first_name) > FieldValidators._FIRSTNAME_LEN_MAX:
            raise ValueError(f'Firstname must be between {FieldValidators._FIRSTNAME_LEN_MIN} and {FieldValidators._FIRSTNAME_LEN_MAX} characters long!')
    
    @staticmethod
    def validate_last_name(last_name: str):        
        if len(last_name) < FieldValidators._LASTNAME_LEN_MIN or len(last_name) > FieldValidators._LASTNAME_LEN_MAX:
            raise ValueError(f'Lastname must be between {FieldValidators._LASTNAME_LEN_MIN} and {FieldValidators._LASTNAME_LEN_MAX} characters long!')