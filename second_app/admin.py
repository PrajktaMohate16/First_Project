from django.contrib import admin

# Register your models here.
from second_app.models import College,Department,Principal,Student,Subjects

admin.site.register([College,Department,Principal,Student,Subjects])