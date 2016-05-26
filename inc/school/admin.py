from django.contrib import admin
from .models import School, ClassRoom, Student

class SchoolAdmin(admin.ModelAdmin):
	list_display = ['school']

class ClassRoomAdmin(admin.ModelAdmin):
	list_display = ['class_room', 'school']

class StudentAdmin(admin.ModelAdmin):
	list_display = ['student', 'class_room']

admin.site.register(School, SchoolAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Student, StudentAdmin)

# Register your models here.
