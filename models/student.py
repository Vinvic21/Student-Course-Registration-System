from models.person import Person

class Student(Person):
    def __init__(self, student_ID, name, email, phone_number):
        super().__init__(name, email, phone_number)
        self.student_ID = student_ID
       
    @property
    def student_ID(self):
        self._student_ID 
    @student_ID.setter
    def name(self, value):
        if not value:
            raise ValueError("student ID cannot be empty")
        self._name = value
   

    
