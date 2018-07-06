from django.contrib import admin
from .models import Course, CourseOutcomes, CourseEnrollment
admin.site.register(Course)
admin.site.register(CourseOutcomes)
admin.site.register(CourseEnrollment)