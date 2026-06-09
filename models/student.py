from models.person import Person

class Student(Person):
    def __init__(self, student_ID, name, email, phone_number):
        super().__init__(name, email, phone_number)
        self.student_ID = student_ID
       
    @property
    def student_ID(self):
        return self._student_ID 
    @student_ID.setter
    def student_ID(self, value):
        value = value.strip()
        if not value:
            raise ValueError("student ID cannot be empty")
        if not value.isdigit():
            raise ValueError("student ID must contain only digits.")
        self._student_ID = value
   

    
