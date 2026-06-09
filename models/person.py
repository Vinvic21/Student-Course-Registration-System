class Person:
    def __init__(self,  name, email, phone_number):
        
        self.name = name
        self.email = email
        self.phone_number = phone_number
    @property
    def name(self):
        self._name 
    @name.setter
    def name(self, value):
        if not self.name:
            raise ValueError("Name cannot be empty")
        self._name = value
    @property
    def email(self):
        self._email
    @email.setter
    def email(self, value):
        if "@" not in self.email:
            raise ValueError("Email must contain @")
        self._email = value

