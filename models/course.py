class Course:
    def __init__(self, course_ID, course_name, trainer_name, capacity, ):
        self.course_ID = course_ID
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = capacity
        self. enrolled = 0
    
    @property
    def course_ID(self):
        return self._course_ID
    @course_ID.setter
    def course_ID(self, value):
        if not value:
            raise ValueError("Course Id cannot be empty")
        self._course_ID = value
    
    @property
    def course_name(self):
        return self._course_name
    @course_name.setter
    def course_name(self, value):
        if not value:
            raise ValueError("Course Name cannot be empty")
        self._course_name = value

    @property
    def trainer_name(self):
        return self._trainer_name
    @trainer_name.setter
    def trainer_name(self, value):
        if not value:
            raise ValueError("Trainer cannot be empty")
        self._trainer_name = value


    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, value):
        if not value:
            raise ValueError("Capacity cannot be empty")
        self._capacity = value
    def add_student(self):
        if self.enrolled >= self.capacity:
            raise ValueError(" Course is full.")
        self.enrolled += 1

