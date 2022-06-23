from django.db import models
from django.forms import ValidationError

# Create your models here.
############-----------Employee model----------###############

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,default=True)
    age = models.IntegerField()
    salary = models.FloatField()
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "Employee_table"

    def __str__(self):
        return self.first_name

############-----------Student model----------###############


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.FloatField()
    is_active = models.BooleanField(default=True)
    Department = models.ForeignKey("Department",on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "Students"

    def __str__(self):
        return self.name

#############--------------College model------------------##############

class CommonField(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

#############--------------College model------------------##############

class College(CommonField):
    address = models.CharField(max_length=100 ,null=True,unique=True)

    class Meta:
        db_table = "College"

#############--------------principal model------------------##############


class Principal(CommonField):
    experience = models.IntegerField(null=True)
    college = models.OneToOneField(College,on_delete=models.CASCADE,default=True)

    class Meta:
        db_table = "Principal"

#############--------------Department model------------------##############

class Department(CommonField):
    name = models.CharField(max_length=100,unique=True,db_column="Dept_name")
    intake = models.IntegerField()
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "Depts"

#############--------------Subjects model------------------##############

class Subjects(CommonField):
    is_practical = models.BooleanField(db_column="IsPractical", null=True)
    total_marks = models.IntegerField(default=True)
    student = models.ManyToManyField(Student)

    class Meta:
        db_table = "Subjects"


#############--------------car model------------------##############

class Car(models.Model):
    car_id = models.CharField(primary_key=True,max_length=6)
    price = models.FloatField(null=True)

    class Meta:
        db_table = "Car"

    def save(self, *args, **kwargs):
        if not self.car_id:
            raise ValidationError("car_id should be passed while creating Car objects....!")
        super(Car, self).save(*args, **kwargs)