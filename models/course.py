class Course:
    def __init__(self, course_ID, course_name, trainer_name, capacity, ):
        self.course_ID = course_ID
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = capacity
    
    @property
    def course_ID(self):
        self._course_ID
    @course_ID.setter
    def course_ID(self, value):
        if not self.course_ID:
            raise ValueError("Course Id cannot be empty")
        self._course_ID = value

