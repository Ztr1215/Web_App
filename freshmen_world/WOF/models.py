from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class StudentUser(models.Model):
    firstName = models.CharField(max_length=40, unique = False)
    secondName = models.CharField(max_length=40, unique = False)
    password = models.CharField(max_length=20, unique = True)
    email = models.CharField(max_length=60, unique = True)
    university = models.CharField(max_length=80, unique = False)
    degree = models.CharField(max_length=30, unique = False)
    level = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'StudentUsers'

    def __str__(self):
        return self.email


class Task(models.Model):
    name=models.CharField(max_length=40, unique = False)
    completed= models.BooleanField(default=False);
    dueDate= models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    timePlanned= models.TimeField(auto_now=False, auto_now_add=False);

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name


class AdminUser(models.Model):
    firstName = models.CharField(max_length = 40,unique = False)
    secondName = models.CharField(max_length = 40,unique = False)
    password = models.CharField(max_length = 20,unique = False)
    email = models.CharField(max_length = 60,unique = True)
    university = models.CharField(max_length = 80,unique = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Admin Users'
        
    def __str__(self):
        return self.email
        

class Course(models.Model):
    name = models.CharField(max_length = 80,unique = True)
    level = models.IntegerField(unique = False)
    credits = models.IntegerField(unique = False)
    courseConvener = models.CharField(max_length = 90, unique = False)
    courseNumber = models.CharField(max_length = 30, unique = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)    
    
    class Meta:
        verbose_name_plural = 'Courses'
        
    def __str__(self):
        return self.name
        
           
class University(models.Model):
    name = models.CharField(max_length = 80,unique = False)
    Location = models.CharField(max_length = 80, unique = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)    
    
    class Meta:
        verbose_name_plural = 'Universites'
        
    def __str__(self):
        return self.name


