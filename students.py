#!/usr/bin/env python3

class Student:
    #constructor for student objects
    def __init__(self, first_name, last_name, ID, school_name, grade_level):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.school_name = school_name
        self.grade_level = grade_level

    #get methods for the Student class
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_ID(self):
        return self.ID

    def get_school_name(self):
        return self.school_name

    def get_grade_level(self):
        return self.grade_level


#subclass of students
class CollegeStudent(Student):
    def __init__(self, first_name, last_name, ID, school_name, grade_level, major, grad_date):

        #call superclass constructor first
        super(). __init__(first_name, last_name, ID, school_name, grade_level)

        #new subclass attributes
        self.major = major
        self.grad_date = grad_date

    #getters for new subclass attributes
    def get_grad_date(self):
        return self.grad_date

    def get_major(self):
        return self.major


    #subclass method
    def panic(self):
        print("AHHHHHHHHHHHHH! I AM SO STRESSED!")

    
