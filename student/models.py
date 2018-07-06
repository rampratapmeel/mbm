from django.db import models
from user.models import User
from program.models import Program
from department.models import Department
from enum import Enum
from course.models import Course
# Create your Student models here.

class Semester(Enum):
    SEM_1 = '1st Semester'
    SEM_2 = "2nd Semester"
    SEM_3 = "3rd Semester"
    SEM_4 = "4th Semester"
    SEM_5 = "5th Semester"
    SEM_6 = "6th Semester"
    SEM_7 = "7th Semester"
    SEM_8 = "8th Semester"


class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Semester],default=Semester.SEM_1)
    program = models.ForeignKey(Program, on_delete=None)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_admission = models.DateField()
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    area_of_interest = models.TextField()
    carrier_objective = models.TextField()

    def __str__(self):
        return self.user.user_name