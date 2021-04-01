from django.db import models
from users.models import *
from sacco.models import *

# Create your models here.

class EducationDepartment(models.Model):
	sacco =  models.ForeignKey(SACCO, on_delete=models.CASCADE, ,default=None)
	name = models.CharField(null=True ,blank=True,max_length=20)
	mission =models.TextField(null=True ,blank=True)
	vision =models.TextField(null=True ,blank=True)
	statement =models.TextField(null=True ,blank=True)
	image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	def __str__(self):
		return self.name

class Tutor(models.Model):
	tutor_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	profile = models.ForeignKey(SaccoStaffMember, related_name="tutor", verbose_name="Tutor Account", on_delete = models.CASCADE,null=True, blank=True,default=None)
	sacco = models.ForeignKey(SACCO, on_delete = models.CASCADE,null=True, blank=True,default=None)
	education_department =  models.ForeignKey(EducationDepartment, on_delete=models.CASCADE,null=True ,blank=True,default=None)
	signup_date = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.profile.user.first_name


class Student(models.Model):
	student_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	profile = models.ForeignKey(AccountUser, related_name="student_profile", on_delete = models.CASCADE,null=True, blank=True,default=None)
	sacco = models.ForeignKey(SACCO, on_delete = models.CASCADE,null=True, blank=True,default=None)
	education_department =  models.ForeignKey(EducationDepartment, on_delete=models.CASCADE,null=True ,blank=True,default=None)
	registration_date = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.profile.user.first_name

class Course(models.Model):
	instructor = models.ForeignKey(EducationDepartment, related_name="education_department",default=None, verbose_name="Education Department", on_delete = models.CASCADE,null=True, blank=True)
	course_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	course_name = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	lead_tutor = models.ForeignKey(Tutor, related_name="lead_tutor", verbose_name="Tutor", on_delete = models.CASCADE,null=True, blank=True,default=None)
	education_department =  models.ForeignKey(EducationDepartment, on_delete=models.CASCADE,null=True ,blank=True)
	course_length = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	
	def __str__(self):
		return self.course_name


class Class(models.Model):
	class_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	instructor = models.ForeignKey(Tutor, related_name="class_instructor", verbose_name="Class Instructor", on_delete = models.CASCADE,null=True, blank=True,default=None)
	course = models.ForeignKey(Course, related_name="class_course", verbose_name="Course", on_delete = models.CASCADE,null=True, blank=True,default=None)
	students = models.ManyToManyField(Student)
	def __str__(self):
		return self.course.course_name

class Survey(models.Model):
	survey_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	survey_name = models.CharField(max_length=100, null=True, blank=True,db_index=True)

	def __str__(self):
		return self.survey_name

class SurveyItem(models.Model):
	survey = models.ForeignKey(Survey, related_name="survey", verbose_name="Survey", on_delete = models.CASCADE,null=True, blank=True,default=None)
	question =models.TextField(null=True ,blank=True)
	answer =models.TextField(null=True ,blank=True)

	def __str__(self):
		return self.survey.survey_name


class Module(models.Model):
	module_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	module_name = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	course = models.ForeignKey(Course, related_name="course", verbose_name="Course", on_delete = models.CASCADE,null=True, blank=True,default=None)
	tutor = models.ForeignKey(Tutor, related_name="module_tutor", verbose_name="Tutor", on_delete = models.CASCADE,null=True, blank=True,default=None)
	decription =models.TextField(null=True ,blank=True)
	intro =models.TextField(null=True ,blank=True)
	module_length = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	upload_date = models.DateTimeField(auto_now=True)

class ModuleItems(models.Model):
	module = models.ForeignKey(Module, related_name="module", verbose_name="Course", on_delete = models.CASCADE,null=True, blank=True,default=None)
	files = models.FileField(blank=True, null=True)
	notes = models.TextField(null=True ,blank=True)
	upload_date = models.DateTimeField(auto_now=True)

