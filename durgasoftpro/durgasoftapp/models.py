from django.db import models

class ContactData(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()

class FeedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    time = models.DateField()
    feedback = models.CharField(max_length=500)