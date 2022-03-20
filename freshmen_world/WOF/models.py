from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class University(models.Model):
    name = models.CharField(max_length = 80,unique = True)
    location = models.CharField(max_length = 80, unique = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(University, self).save(*args, **kwargs)    
     
    class Meta:
        verbose_name_plural = 'Universites'
        
    def __str__(self):
        return self.name

class StudentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    degree = models.CharField(max_length=80, unique = False, default="", null=True)
    level = models.IntegerField(default=0, null=True)

    class Meta:
        verbose_name_plural = 'Student Users'

    def __str__(self):
        return self.user.username


class Task(models.Model):
    name = models.CharField(max_length=40, unique = True)
    completed = models.BooleanField(default=False);
    dueDate = models.DateField(
        verbose_name = ("Creation date"), auto_now_add=False, null=True
    )
    timePlanned = models.TimeField(auto_now=False, auto_now_add=False);

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name


class AdminUser(models.Model):
    # firstName = models.CharField(max_length = 40,unique = False)
    # secondName = models.CharField(max_length = 40,unique = False)
    # password = models.CharField(max_length = 20,unique = False)
    # email = models.CharField(max_length = 60,unique = True)
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
    university = models.ForeignKey(University, on_delete=models.CASCADE , null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)    
    
    class Meta:
        verbose_name_plural = 'Courses'
        
    def __str__(self):
        return self.name
        
           

