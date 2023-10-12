from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = ['name','roll_number','department']
