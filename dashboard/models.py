from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=50)
