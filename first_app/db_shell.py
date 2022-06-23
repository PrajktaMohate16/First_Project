# exec(open(r"D:\Django\First_Project\first_app\db_shell.py").read())


from first_app.models import Student,Empolyee

############-----Fetching all data by using all()method-----############

# all_data = Student.objects.all()  # gives all data
# print(all_data)   #<QuerySet [<Student: aaa>, <Student: bbb>, <Student: ccc>, <Student: ddd>, <Student: eee>, <Student: eee>, <Student: fff>]>
# print(type(all_data))   # <class 'django.db.models.query.QuerySet'>

# for i in all_data:
#     print(i.__dict__)    # gives name of all students

############-----Fetching singal data by using first()method-----############

# singal_data = Student.objects.first()
# print(singal_data)      # getting singal data

############-----Fetching filter data by using filter()-----############

# data = Student.objects.filter(id__gte=20)
# print(data)    # gives data greater than or equal to 3
# for i in data:
#     print(i)
# print(data)    # <QuerySet []>

############-----Fetching singal data by using get()-----############


# data = Student.objects.get(id=5)
# print(data)   # get singal data which id we passed

# if data is not present in the table getmethod  raise error
# try:
#     data = Student.objects.get(id=20)
#     print(data)
# except Student.DoesNotExist as msg:
#     print(msg,"No data")


############-----updating data-----############

# try:
#     data = Student.objects.get(id=3)
#     data.name = "zzz"
#     data.save()
#     print(data)  # commit
# except Student.DoesNotExist:
#     print("no data")


# all_data = Student.objects.get(id=2)
# all_data.get_stud_details()
# print(Student.get_all_stud_details())

# print(Student.get_stud_marks_avg())
# print(Student.get_stud_marks_avg())
# print(Student.get_stud_marks_avg())

# print(Student.get_avg_age())
# print(Student.get_stud_by_name("xxx"))
# print(Student.delete_singal_data("fff"))
# print(Student.increment_marks())
# print(Student.get_stud_age_less_passed_num(25))
# print(Student.get_active_studs())

############-----saving data-----############

# 1]
# By using admin page-- UI --Graphical User Interface

# 2] 
# By using save() method
# all_data = Student.objects.all()
# all_data.save()

# 3]
# By using create() method
# stud = dir(Student.objects)
# print(stud)

############-----count()method-----############
# stud = Student.objects.count()  # gives no of students present
# print(stud)

############-----len()method-----############
# print(len(Student.objects.all()))

############-----Customized model manager-----############
# default
# all_data = Student.objects.all().filter(is_active=True)
# print(all_data)
# print(all_data.query)

# print(Student.active_objects.all())
# print(Student.in_active_objects.all())
# print(Student.objects.all())


# Empolyee.insert_data_into_table()
# all_data = Student.objects.all()
# print(all_data.__dict__)
# print(Empolyee.delect_data())
# print(Empolyee.update_data())
