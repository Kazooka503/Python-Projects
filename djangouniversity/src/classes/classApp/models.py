from django.db import models

# Create your models here.


class DjangoClasses(models.Model):
    title = models.CharField(max_length=100)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=20)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title

