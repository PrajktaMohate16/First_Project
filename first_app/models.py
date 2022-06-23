from django.db import models
from functools import reduce
# Create your models here.


############-----Customized model manager-----############

class ActiveStudManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class InActiveStudManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)

############-----student model-----############

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.FloatField()
    is_active = models.BooleanField(default=True)
    # active_objects = ActiveStudManager()
    # in_active_objects = InActiveStudManager()
    # objects = models.Manager()
    
    class Meta:
        db_table = "Student"

    def __str__(self):
        return self.name

############-----get singal student details-----############

    def get_stud_details(self):
        print(f"""Student ID:- {self.id}
Student Name:- {self.name}
Student Age :- {self.age}
Student Marks :- {self.marks}
""")
    
############-----get all student details-----############

    @classmethod
    def get_all_stud_details(cls):
       all_data = Student.objects.all()
       for data in all_data:
           data.__dict__.pop("_state")
           print(data.__dict__)


############-----get average marks of students(by normal function)-----############

    @classmethod
    def get_stud_marks_avg(cls):
        all_data = Student.objects.all()
        total = 0
        for stud in all_data:
            total += stud.marks 
            avg = total/len(all_data)
        return avg

############-----get average marks of students(by lambda function - using "reduce")-----############

    @classmethod
    def get_stud_marks_avg(cls):
        all_data = cls.objects.all()
        mark_list = []
        for stud in all_data:
            mark_list.append(stud.marks)
            mark_list   
        res = reduce(lambda x,y:x+y,mark_list)
        avg = res/len(mark_list)
        return avg 

############-----get average marks of students(by lambda function - using "map")-----############

    @classmethod
    def get_stud_marks_avg(cls):
        all_data = cls.objects.all()
        mark_list = []
        for stud in all_data:
            mark_list.append(stud.marks)
            res = list(map(lambda x:x,mark_list))
        avg = sum(res)/len(mark_list)
        return avg

############-----get student age which is less than passed number-----############

    @classmethod
    def get_stud_age_less_passed_num(cls,num):
        all_data = cls.objects.all()
        for stud in all_data:
            if stud.age < num:
                stud.__dict__.pop("_state")
                print(stud.__dict__)

############-----get average of student age by using "reduce"-----############

    @classmethod
    def get_avg_age(cls):
        all_data = cls.objects.all()
        age_list = []
        for stud in all_data:
            age_list.append(stud.age)
            res = reduce(lambda x,y : x+y ,age_list)
            avg = res/len(age_list)
            return avg

############-----get student by passing name to function-----############

    @classmethod
    def get_stud_by_name(cls,nm):
        all_data = cls.objects.all()
        for stud in all_data:
            if stud.name == nm:
                stud.__dict__.pop("_state")
                return stud.__dict__
            else:
                pass

############-----deleting singal data and return deleted data-----############

    @classmethod
    def delete_singal_data(cls,nm):
        all_data = cls.objects.all()
        for stud in all_data:
            data_name = stud.__dict__
            if stud.name == nm:
                data_name = stud.name
                stud.delete()
                stud.save()
                print(data_name)
            else:
                pass

############-----getting incremented marks -----############

    @classmethod
    def increment_marks(cls):
        data = cls.objects.filter(id__gte=1)
        for stud in data:
            stud.marks += (stud.marks*(5/100))
            if stud.marks > 100:
                pass
            else:
                print(stud.marks)
                stud.save()

############-----incremented marks-----############

    @classmethod
    def increment_marks(cls):
        all_data = Student.objects.all()
        for stud in all_data:
            stud.marks += (stud.marks*(5/100))
            stud.save()

############-----get active students-----############

    @classmethod
    def get_active_studs(cls):
        all_data = cls.objects.filter(is_active=1)
        return all_data



############-----Employee model-----############

class Empolyee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.FloatField()
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return self.name

############-----delete data from model-----############

    @classmethod
    def delete_data(cls):
        all_data = Empolyee.objects.all()
        all_data.delete()
    
############-----update data in model-----############

    @classmethod
    def update_data(cls):
        obj1 = Empolyee(id=101,name="prajkta",age=23,salary=70000,address="Mumbai")
        obj2 = Empolyee(id=102,name="prajkt",age=23,salary=50000,address="Pune")
        obj3 = Empolyee(id=103,name="pravin",age=23,salary=20000,address="Nahik")
        obj4 = Empolyee(id=104,name="prachi",age=23,salary=90000,address="Nagar")
        obj5 = Empolyee(id=105,name="pradnya",age=23,salary=60000,address="Panvel")
        obj6 = Empolyee(id=106,name="pranav",age=23,salary=30000,address="Dadar")
        obj1.save(),obj2.save(),obj3.save(),obj4.save(),obj5.save(),obj6.save()