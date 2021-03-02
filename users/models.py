from django.db import models
from decimal import Decimal as D
from .UserManager import UserManager
from django.contrib.auth.hashers import get_hasher, identify_hasher
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class MembershipRole(models.Model):
	secretary = 'secretary'
	manager = 'manager'
	tutor = 'tutor'
	student = 'student'
	field_officer = 'field_officer'
	member = 'member'
	USER_GROUP_CHOICES = [
			(student,'student'),
			(member,'member'),
		]
	ROLE_CHOICES = [
			(student,'student'),
			(field_officer,'field_officer'),
			(secretary,'secretary'),
			(manager,'manager'),
			(tutor,'tutor'),
		]
	name = models.CharField(max_length=70, choices=ROLE_CHOICES, default = manager)
	group = models.CharField(max_length=70, choices=USER_GROUP_CHOICES, default = member)

	def __str__(self):
		return self.name

class AccountUser(models.Model):
	# user_role = models.ForeignKey(Role, on_delete = models.CASCADE , null=True, blank=True)
	membership_role = models.ForeignKey(MembershipRole, on_delete = models.CASCADE , null=True, blank=True)
	user = models.ForeignKey(User, on_delete = models.CASCADE , null=True, blank=True)
	category = models.CharField(null=True ,blank=True,max_length=70)
	work_email = models.CharField(null=True ,blank=True,max_length=70)
	personal_email = models.CharField(null=True ,blank=True,max_length=70)
	age = models.IntegerField(null=True ,blank=True)
	city = models.CharField(max_length=70,null=True ,blank=True)
	country = models.CharField(max_length=70,null=True ,blank=True)
	province = models.CharField(max_length=70,null=True ,blank=True)
	home_address =models.TextField(null=True ,blank=True)
	email_confirmed = models.BooleanField(default=False)
	accepted_terms = models.BooleanField(default=False)
	date_birth =models.DateField(null=True ,blank=True)
	phone =models.CharField(null=True ,blank=True,max_length=70)
	whatsapp_number =models.CharField(null=True ,blank=True,max_length=70)
	direct_number =models.CharField(null=True ,blank=True,max_length=70)
	national_id =models.CharField(null=True ,blank=True,max_length=20)
	gender =models.CharField(null=True ,blank=True,max_length=20)
	education_level =models.CharField(null=True ,blank=True,max_length=70)
	marital_status =models.CharField(null=True ,blank=True,max_length=20)
	number_dependants =models.IntegerField(null=True ,blank=True)
	profile_pic = models.ImageField(null=True ,blank=True, upload_to='media/images')
	facebook_url = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	android = models.BooleanField(blank=True, default=False)
	ios = models.NullBooleanField(blank=True, default=False, null=True)
	acceptPush = models.BooleanField(default=False)
	pushToken = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	is_active = models.BooleanField(('active'), default=True)
	is_staff = models.BooleanField(('staff'), default=False)
	objects = UserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	def __str__(self):
		return self.user.first_name
	class Meta:
		verbose_name = ('Sacco Member')
		verbose_name_plural = ('Sacco Members')



