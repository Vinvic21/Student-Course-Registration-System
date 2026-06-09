What was the hardest part of this project?
    the hardest part for me was working with json files. I was getting errors because the json files were empty which was a challenge.

Which classes did you create and why?
    class Person - this acted as a parent class. Had name, email and phone number in which the child classs will inherit
    class Student - this was a child class for class Person. Contained students details which they were already in Parent class, just added student Id and used super() to connect the
    Class course - this had the course details
    class SchoolSystem - this had methods like add student, view students and add course

How does your registration logic prevent duplicate registrations?
    It checks if the student Id or course Id already exists, if yes it stops the program

How does your system check if a course is full?
     I set the enrolled students in that course to start at zero so that every time a student is added to the list the students enrolled is incremented by 1. used if statement to check the if the enrolled students is equal or greater than the capcity if yes the program will stop

What bugs did you face and how did you fix them?
     the bug I faced was validation, it could add an empty name and still  work.
     I had to go one by one through the  validation to ensure all are working as required

Which part of the code would you improve if you had more time?
    email validation. For now it only shows an error message when you fail to use @
    I would have wanted to use regex to ensure the email follows the deired format

