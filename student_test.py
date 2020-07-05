#!/usr/bin/env python3

from students import Student
from students import CollegeStudent

#create student objects
student1 = Student("Lina", "Breunlin", 2055392,
                   "Estrella Mountain Community College", "Senior")

#print student data to console

print("Student Information:")
print("Name:          " + student1.first_name + " " + student1.last_name)
print("Student ID:    " + str(student1.ID))
print("School:        " + student1.school_name)
print("Grade Level:   " + student1.grade_level)

print()
print()

#create college student object
college1 = CollegeStudent("Lina", "Breunlin", 2055392,
                           "Estrella Mountain Community College", "Senior",
                           "Programming and System Analysis", "July 30, 2020")
print("College Student Information:")
print("Name:           " + college1.first_name + " " + student1.last_name)
print("Student ID:     " + str(college1.ID))
print("School:         " + college1.school_name)
print("Grade Level:    " + college1.grade_level)
print("Majorl:         " + college1.major)
print("Graduation Date:" + college1.grad_date)

print()
college1.panic() #access college student only method

