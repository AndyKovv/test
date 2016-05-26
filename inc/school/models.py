from django.db import models


class School(models.Model):
	school = models.CharField(max_length=100)

	def __str__(self):
		return self.school

class ClassRoom(models.Model):
	school = models.ForeignKey(School)
	class_room = models.CharField(max_length=100)

	def __str__(self):
		return self.class_room

	class Meta:
		unique_together = ('class_room', 'school')

class Student(models.Model):
	class_room = models.ForeignKey(ClassRoom)
	student = models.CharField(max_length=100)

	def __str__(self):
		return self.student

	class Meta:
		unique_together = ('student', 'class_room',)

