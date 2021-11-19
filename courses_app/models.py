from django.db import models
from django.db.models.fields.related import ForeignKey

class CourseManager(models.Manager):
    def validator(self,postData):
        errors= {}
        if len(postData['name']) < 5:
            errors['name'] = "name must be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Description must be at least 15 characters"
        return errors

# class DescriptionManager(models.Manager):
#     def description_validator(self,postData):
#         errors= {}
#         if len(postData['description']) < 15:
#             errors['description'] = "Description must be at least 15 characters"
#         return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()

class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE,primary_key=True)
    body = models.TextField()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add = True)
    course = models.ForeignKey(Course,related_name="comments",on_delete = models.CASCADE)