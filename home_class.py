class Home:
    # Class to create a home oject
    def __init__(self, home_id, address, city, state, zip_code, model_name, sqft, status):
        self.home_id = home_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.model_name = model_name
        self.sqft = sqft
        self.status = status 
        
    def __str__(self):
        # Returns the string version of the object
        return str({'Home ID': self.home_id,
                    'Address': self.address,
                    'City': self.city,
                    'State': self.state,
                    'Zip Code': self.zip_code,
                    'Model Name': self.model_name,
                    'SQFT': self.sqft,
                    'Status': self.status})

    def update(self, attrs):
        # Updates attributes
        # Accepts a dictionary of attributes to update
        for key, value in attrs.items():
            if key in self.__dict__:
                setattr(self, key, value)