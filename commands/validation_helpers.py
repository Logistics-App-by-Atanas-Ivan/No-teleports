class ValidationHelpers:
      
    def validate_params_count(self, params, count):
        if len(params) != count:
            raise ValueError(
                f'Invalid number of arguments. Expected: {count}; received: {len(params)}.")')

    def try_parse_float(self, s):
        try:
            return float(s)
        except:
            raise ValueError('Invalid value. Should be a number.') #Check if the message can be improved & includes the variable name 'Invalid value for {variable_name}. Should be a number.'

    def try_parse_int(self, s):
        try:
            return int(s)
        except:
            raise ValueError('Invalid value for mililitres. Should be an integer.') #Check if the message can be improved & includes the variable name 'Invalid value for {variable_name}. Should be an integer.'
        
    def location_exists(self, location, start =True):
        #use another class to check later? or move it to app data
        locations = ['perth', 'darwin', 'alice springs', 'adelaide', 'melbourne', 'sydney', 'brisbane']
        if location.lower() not in locations:
            if start:
                raise ValueError('Please enter a valid start location.')
            else:
                raise ValueError('Please enter a valid end location.')
        return location.title()