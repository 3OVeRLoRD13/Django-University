from django.db import models

# Create your models here.


class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student_ID = models.CharField(max_length=255)
    Course_ID = models.CharField(max_length=255)
    Master_ID = models.CharField(max_length=255)
    semegter = models.CharField(max_length=255)
    mark = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    
    def __str__(self):
        return self.student_ID + self.Course_ID


class Course(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    
    def __str__(self):
        return self.title + self.department


class Master(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    national_ID = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    department_ID = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    room = models.CharField(max_length=255)

    
    def __str__(self):
        return self.first_name + self.last_name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    national_ID = models.CharField(max_length=10, default='0')
    phone_number = models.CharField(max_length=11, default='0')
    
    
    def __str__(self):
        return self.first_name + self.last_name
    