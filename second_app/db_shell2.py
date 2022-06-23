# exec(open(r"D:\Django\First_Project\second_app\db_shell2.py").read())


from second_app.models import *
from django.db.models import Q
from django.db.models import Avg,Min,Max,Sum,Count
from django.contrib.auth.models import User

# emp1 = Employee.objects.create(name="prajkta",age=23,salary=70000,address="Mumbai")
# emp2 = Employee.objects.create(name="prajkt",age=25,salary=65000,address="Nashik")
# emp3 = Employee.objects.create(name="prachi",age=27,salary=35000,address="Thane")
# emp4 = Employee.objects.create(name="pratik",age=29,salary=98000,address="Panvel")
# emp5 = Employee.objects.create(name="prashant",age=26,salary=40000,address="Dhule")

# print(emp)

# emp = Employee(name="prajkta",age=23,salary=70000,address="Mumbai")
# emp.save()
# print(emp)

#DJANGO ORM COOKBOOK:-
#########------to find the query associated with a queryset------#########
# EXAMPLE:-1
# queryset = Employee.objects.all()
# print(queryset.query)

# OUTPUT:-
# SELECT `Employee_table`.`id`, `Employee_table`.`name`, `Employee_table`.`age`, 
# `Employee_table`.`salary`, `Employee_table`.`address` FROM `Employee_table`

# EXAMPLE:-2
# queryset = Employee.objects.filter(id__gt=5)
# print(queryset)  #<QuerySet [<Employee: prachi>, <Employee: pratik>, <Employee: prashant>]>
# print(queryset.query) 

# OUTPUT:-
#SELECT `Employee_table`.`id`, `Employee_table`.`name`, `Employee_table`.`age`, 
# `Employee_table`.`salary`, `Employee_table`.`address` FROM `Employee_table` WHERE `Employee_table`.`id` > 5

#########------HOW TO USE OR QUERY IN DJNAGO ORM------#########

# provides two options:-
# 1.queryset_1 | queryset_2

# Example:-
# queryset = Employee.objects.filter(name__startswith="p")| Employee.objects.filter(name__startswith="S")
# print(queryset)

# 2.filter(Q(<condition_1>)|Q(<condition_2>)
# queryset = Employee.objects.filter(Q(name__startswith="P")|Q(name__startswith="S"))
# print(queryset)


#########------HOW TO USE AND QUERY IN DJNAGO ORM------#########

# Django provides 3 options:-
# 1.filter(<condition_1>, <condition_2>)
# query1 = Employee.objects.filter(first_name__startswith="S",last_name__startswith="T")[0]
# print(query1)
# q = Employee.objects.filter(first_name__startswith="P",last_name__startswith="M")[0]
# print(q)

# 2.queryset_1 & queryset_2
# query_set = Employee.objects.filter(first_name__startswith="p") & Employee.objects.filter(last_name__startswith="B")
# print(query_set)

# 3.filter(Q(<condition_1>) & Q(<condition_2>))
# query = Employee.objects.filter(Q(first_name__startswith="p")& Q(last_name__startswith="T"))
# print(query)


#########------HOW TO USE not QUERY IN DJNAGO ORM------#########

# 1.exclude(<condition>)
# query = Employee.objects.all().exclude(id__lt=5)
# print(query)
# q = Employee.objects.filter().exclude(id__gte=6)
# print(q)

# 2.filter(~Q(<condition>))
# queryset = Employee.objects.filter(~Q(id__gt=4))
# print(queryset)

#######-----union of two querysets from same or different models-----###########

# q1 = Employee.objects.filter(id__gte=5)
# print(q1)
# q2 = Employee.objects.filter(id__lte=5)
# print(q2)
# print(q1.union(q2))

# union1 = Employee.objects.all().values_list("id","age").union(Student.objects.all().values_list("id","age")) 
# print(union1)

##########------- How to select some fields only in a queryset-----########

# emp = Employee.objects.all().values("id")
# print(emp)
# emp1 =  Employee.objects.all().values_list("id","first_name","age","salary","address","last_name")
# print(emp1)

# emp2 = Employee.objects.filter(first_name__startswith="P").only("first_name","last_name")
# print(emp2)

############--------count()--------#############

# stud = Student.objects.all().count()
# print(stud)  # gives no of rows present in model

############--------Bulk create--------#############

# emp = Employee.objects.bulk_create([Employee(first_name="Raj",last_name="Bhor",age="24",address="Sangali",salary=78000)])
# print(emp)

############--------limiting query set--------#############

# emp1 = Employee.objects.all()[:]
# emp2 = Employee.objects.all()[:4]
# emp3 = Employee.objects.all()[0:8]
# emp4 = Employee.objects.all()[0:8:2]
# emp5 = Employee.objects.all()[0]
# print(emp5)

############-------- order a QuerySets in ascending or descending order----###########

# emp1 = Employee.objects.all().order_by("age")
# emp2 = Employee.objects.all().order_by("-salary")
# print(emp2)

############--------exact()----###########

# iexact = case insensitive
# emp = Employee.objects.filter(first_name__exact="prajkta")
# emp1 = Employee.objects.filter(first_name__iexact="prajkta")
# print(emp1)

############--------contains()----###########
# icontains = case sensitive version
# emp = Employee.objects.filter(first_name__contains="achin")
# emp1 = Employee.objects.filter(first_name__contains="i")
# print(emp1)

#########-------How to group record in Django ORM--------##########

# emp1 = Employee.objects.all().aggregate(Avg("id"))
# print(emp1)
# emp2 = Employee.objects.all().aggregate(Min("id"))
# print(emp2)
# emp3 = Employee.objects.all().aggregate(Max("age"))
# print(emp3)
# emp4 = Employee.objects.all().aggregate(Sum("salary"))
# print(emp4)
# emp5 = Employee.objects.all().count()
# print(emp5)

# all_users = User.objects.all()
# print(type(all_users[0]))   #<class 'django.contrib.auth.models.User'>

# c1 = Car.objects.create(car_id="PM0002",price=800000)
# c1.save()

#########-------Orderd by in Django ORM--------##########

# data = Student.objects.all().order_by("name")  #--- gives values in ascending order
# print(data.query)

# data = Student.objects.all().order_by("-name")  #---gives values in descending order
# print(data.query)

#########-------Fetch principal from college Django model--------##########

try:
    c1 = College.objects.get(name="D Y Patil")
except College.DoesNotExist:
    print("College does not exist...!")
# else:
    # print(c1.principal)
    # print(dir(c1))

#########-------Fetch department from college Django model--------##########

# c1 = College.objects.get(name="D Y Patil")
# print(dir(c1))
# print(c1.department_set.all())

#########-------Fetch department from college Django model--------##########

# d1 = Department.objects.get(name="IT")
# print(d1.student_set.all())

#########-------Fetch department from college Django model--------##########

# s1 = Student.objects.get(name="bbb")
# print(dir(s1))
# print(s1.subjects_set.all())

#########-------Fetch Student from college Django model--------##########

# code:-1
# c1 = College.objects.get(name="D Y Patil")
# depts = c1.department_set.get(name="Civil")
# studs = depts.student_set.all()
# print(studs)

# code:-1
# def get_all_studs_from_college():
#     student_lst = []
#     c1 = College.objects.get(name="Sinhgad")
#     depts = c1.department_set.all()
#     for dept in depts:
#         studs = dept.student_set.all()
#         student_lst.extend(studs)
#     return student_lst

# print(get_all_studs_from_college())

#########-------Fetch Subjects from college Django model--------##########

# def get_sub_from_college():
#     student_lst = []
#     subject = set()
#     c1 = College.objects.get(name="D Y Patil")
#     depts = c1.department_set.all()
#     for dept in depts:
#         studs = dept.student_set.all()
#         student_lst.extend(studs)
#         for stud in student_lst:
#             sub = stud.subjects_set.all()
#             subject.update(sub)
#         return subject

# print(get_sub_from_college())

#########-------Fetch Department from students Django model--------##########

# s1 = Student.objects.get(id=1)
# print(s1.Department)

# s2 = Student.objects.get(id=5)
# print(s2.Department.college.principal)

# s3 = Student.objects.all()
# for i in s3:
#     print(i.Department)


#########-------Fetch Student from subjects Django model--------##########

# s = Subjects.objects.first()
# print(dir(s))
# print(s.student.all())
# print(s.student.filter(name__startswith="b"))
# print(s.student.filter(name__endswith="x"))
# print(s.student.filter(name__contains="b"))
# print(s.student.filter(name__istartswith="X"))      # i- caseinsensitive


# s1 = Subjects.objects.filter(student__name="aaa")
# print(s1)

# s1 = Subjects.objects.filter(student__Department__name="IT")
# print(s1)

# subs = Subjects.objects.filter(student__Department__college__name="D Y Patil")
# print(subs)

# sub = Subjects.objects.filter(student__Department__college__principal__name="pravin")
# print(sub)

# sub = Subjects.objects.filter(student__Department__id="1")
# print(sub)

# sub = Subjects.objects.filter(student__Department__college=1)  # by default it takes __id
# print(sub)

# sub = set(Subjects.objects.filter(student__Department__college__name="Sinhgad"))  # convert into set to avoid duplicate entry
# print(sub)

# sub = Subjects.objects.filter(student__Department__college__name="D Y Patil").values("total_marks")
# print(sub)

# sub = Subjects.objects.filter(student__Department__college__principal__name="Prajkta").values_list("name","total_marks")
# print(sub)

#########-------creating college--------##########

# c1 = College.objects.create(name="Wadia College",address="Lonavala")
# c1 = College.objects.get(name="Wadia College")
# print(c1)

#########-------creating principal--------##########

# p1 = Principal.objects.create(name="Sai",college=c1)
# print(p1)

# p2 = Principal.objects.create(name="Raj",college_id=3)
# print(p2)

#########-------creating principal--------##########
# d1 = Department.objects.create(name="Computer",intake=80,college_id=3)
# print(d1)

#########-------add subjects into student--------##########

stud1 = Student.objects.create(name="hhh",age=25,marks=85)
stud2 = Student.objects.create(name="iii",age=25,marks=85)
# print(stud1,stud2)

# print(stud1)

s1 = Subjects.objects.create(name="Python")
# print(s1)

# s1.student.add(stud1)  #singal and multiple objects can be add
s1.student.remove(stud2)

#########-------Fetch college from students Django model--------##########

# s = Student.objects.first()
# print(s.Department.college.principal)

#########-------Fetch college from subjects Django model--------##########

# s1 = Subjects.objects.first()
# print(s1.student.first().Department.college.principal)


# exec(open(r"D:\Django\First_Project\second_app\db_shell2.py").read())
