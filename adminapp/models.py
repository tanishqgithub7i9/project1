from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=20,unique=True)
    desc = models.CharField(max_length=255)



class Branch(models.Model):
    name = models.CharField(max_length=30,unique=True)

class Course(models.Model):
    name = models.CharField(max_length=30,unique=True)

class Session(models.Model):
    name = models.CharField(max_length=30,unique=True)

class study(models.Model):
    branch = models.CharField(max_length=30)
    session = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    file_name = models.CharField(max_length=30)
    file = models.FileField(max_length=255,upload_to="sthyudy")