from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['stid', 'name_prefix', 'first_name', 'last_name', 'age']
    search_fields = ['first_name', 'last_name']


@admin.register(models.Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'subject_name', 'teacher_name']
    search_fields = ['subject_code', 'subject_name', 'teacher_name']