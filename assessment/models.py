from django.db import models
from enum import Enum
from user.models import User
from course.models import Course, CourseOutcomes
from student.models import Student
from faculty.models import Faculty
from datetime import date


class QuestionType(Enum):
    T = "Theory"
    P = "Practical"


class AssessmentType(Enum):
    Int = "Internal"
    M = "Main"


class Assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=None)
    type = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in AssessmentType], default=AssessmentType.Int)
    start_date = models.DateField(default=date.today)
    duration = models.DurationField()
    faculty_id = models.ForeignKey(Faculty, on_delete=None)
    year = models.PositiveSmallIntegerField()




class AssessmentQuestion(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=12, choices=[(tag.name, tag.value) for tag in QuestionType], default=QuestionType.P)
    text = models.TextField()
    max_marks = models.PositiveSmallIntegerField()
    question_order = models.PositiveSmallIntegerField()
    marking_scheme = models.TextField()
    outcome = models.ForeignKey(CourseOutcomes, on_delete=None)



class AssessmentResult(models.Model):
    question = models.ForeignKey(AssessmentQuestion, on_delete=None,)
    student = models.ForeignKey(Student, on_delete=None)
    obtained_marks = models.PositiveSmallIntegerField()

