from django.db import models
from users.choices import *
from users.models import AccountUser, MembershipRole

# Create your models here.
class Country(models.Model): 
	name = models.CharField(max_length=200, choices=countries_choices, default='Zimbabwe')
	official_language = models.TextField(null=True ,blank=True)
	flag = models.ImageField(null=True ,blank=True, upload_to='media/images/countries/flags')
	# location = models.PointField(null=True, blank=True)

	def __str__(self):
		return self.name

# Create your models here.
class City(models.Model): 
	name = models.CharField(max_length=200)
	country = models.CharField(max_length=200, choices=countries_choices, default='Zimbabwe')
	state = models.CharField(max_length=200, null=True ,blank=True)
	updated_state = models.CharField(max_length=200, null=True ,blank=True)
	# country = models.ForeignKey(Country, on_delete = models.CASCADE , null=True, blank=True)
	official_language = models.TextField(null=True ,blank=True)
	flag = models.ImageField(null=True ,blank=True, upload_to='media/images/countries/flags')
	# location = models.PointField(null=True, blank=True)

	def __str__(self):
		return self.name

		
class NationalBoards(models.Model):
	board_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	board_name = models.CharField(max_length=70,null=True ,blank=True)
	country = models.ForeignKey(Country, on_delete = models.CASCADE , null=True, blank=True)
	registered_by_id = models.CharField(max_length=70,null=True ,blank=True)
	total_branches =models.IntegerField(null=True ,blank=True)
	logo_lg_dn = models.ImageField(null=True ,blank=True, upload_to='media/board_images')
	logo_xl_up = models.ImageField(null=True ,blank=True, upload_to='media/board_images')
	logo_lg_up = models.ImageField(null=True ,blank=True, upload_to='media/board_images')
	
	hq_city = models.CharField(max_length=70,null=True ,blank=True)
	address =models.TextField(null=True ,blank=True)
	phone =models.CharField(null=True ,blank=True,max_length=70)
	logo = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	icon = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	image1 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	statement =models.TextField(null=True ,blank=True)
	acceptPush = models.BooleanField(default=False)
	pushToken = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	is_active = models.BooleanField(('active'), default=True)
	def __str__(self):
		return self.business_name


class SACCO(models.Model):
	sacco_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	country = models.ForeignKey(Country, on_delete = models.CASCADE , null=True, blank=True)
	affliate_to_NB = models.BooleanField(default=False)
	name = models.CharField(max_length=70,null=True ,blank=True)
	registered_by_id = models.CharField(max_length=70,null=True ,blank=True)
	total_branches =models.IntegerField(null=True ,blank=True)
	logo_lg_dn = models.ImageField(null=True ,blank=True, upload_to='media/board_images')
	logo_xl_up = models.ImageField(null=True ,blank=True, upload_to='media/board_images')
	logo_lg_up = models.ImageField(null=True ,blank=True, upload_to='media/board_images')
	
	city = models.CharField(max_length=70,null=True ,blank=True)
	province = models.CharField(max_length=70,null=True ,blank=True)
	address =models.TextField(null=True ,blank=True)
	phone =models.CharField(null=True ,blank=True,max_length=70)
	logo = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	icon = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	image1 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	statement =models.TextField(null=True ,blank=True)
	acceptPush = models.BooleanField(default=False)
	pushToken = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	is_active = models.BooleanField(('active'), default=True)
	def __str__(self):
		return self.name


class Objective(models.Model):
    video_url = models.TextField(null=True ,blank=True)
    image = models.ImageField(null=True ,blank=True, upload_to='media/images')
    title =models.TextField(null=True ,blank=True)
    text =models.TextField(null=True ,blank=True)
    def __str__(self):
        return self.title

		
class Department(models.Model):
	sacco =  models.ForeignKey(SACCO, related_name="sacco", verbose_name="Department", on_delete=models.CASCADE, default=0)
	name = models.CharField(null=True ,blank=True,max_length=20)
	mission =models.TextField(null=True ,blank=True)
	vision =models.TextField(null=True ,blank=True)
	statement =models.TextField(null=True ,blank=True)
	image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	def __str__(self):
		return self.name


class NationalStaffMember(models.Model):
	board = models.ForeignKey(NationalBoards, on_delete = models.CASCADE , null=True, blank=True)
	profile = models.OneToOneField(AccountUser, on_delete = models.CASCADE)
	department = models.ForeignKey(Department, on_delete = models.CASCADE)
	role = models.ForeignKey(MembershipRole, on_delete = models.CASCADE)
	appointment_date = models.DateTimeField(auto_now_add=True, blank=True)
	valid_till_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_executive = models.BooleanField(('executive'), default=False)

	def __str__(self):
		return self.profile.user.username

class SaccoMember(models.Model):
	sacco = models.ForeignKey(SACCO, on_delete = models.CASCADE,null=True, blank=True)
	member_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	profile = models.OneToOneField(AccountUser, on_delete = models.CASCADE)


class SaccoStaffMember(models.Model):
	sacco = models.ForeignKey(SACCO, on_delete = models.CASCADE,null=True, blank=True)
	staff_id = models.CharField(max_length=100, null=True, blank=True,db_index=True)
	profile = models.OneToOneField(SaccoMember, on_delete = models.CASCADE)
	department = models.ForeignKey(Department, on_delete = models.CASCADE)
	role = models.ForeignKey(MembershipRole, on_delete = models.CASCADE)
	appointment_date = models.DateTimeField(auto_now_add=True, blank=True)
	valid_till_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_executive = models.BooleanField(('executive'), default=False)

	def __str__(self):
		return self.profile.user.username

class ArticleCategory(models.Model):
	publication_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_active = models.BooleanField(('active'), default=False)
	name = models.CharField(max_length=200, null=True ,blank=True)

class Article(models.Model):
	category = models.ForeignKey(ArticleCategory, on_delete = models.CASCADE,null=True, blank=True)
	publisher = models.ForeignKey(SACCO, on_delete = models.CASCADE,null=True, blank=True)
	author = models.ForeignKey(SaccoMember, on_delete = models.CASCADE)
	head_line = models.CharField(max_length=200)
	sub_head_line1 = models.CharField(null=True ,blank=True,max_length=200)
	sub_head_line2 = models.CharField(null=True ,blank=True,max_length=200)
	sub_head_line3 = models.CharField(null=True ,blank=True,max_length=200)
	intro =models.TextField(null=True ,blank=True)
	summary =models.TextField(null=True ,blank=True)
	article_paragraph1 =models.TextField(null=True ,blank=True)
	article_paragraph2 =models.TextField(null=True ,blank=True)
	article_paragraph3 =models.TextField(null=True ,blank=True)
	blockquote1 =models.CharField(null=True ,blank=True,max_length=50)
	blockquote2 =models.CharField(null=True ,blank=True,max_length=50)
	blockquote3 =models.CharField(null=True ,blank=True,max_length=50)
	last_accessed = models.DateTimeField(null=True ,blank=True)
	publication_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_active = models.BooleanField(('active'), default=False)
	main_image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	center_image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	cover_image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
	
	def __str__(self):
		return self.head_line

class ArticleComment(models.Model):
	Article = models.ForeignKey(Article, on_delete = models.CASCADE)
	comment =models.TextField(null=True ,blank=True)
	publication_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_active = models.BooleanField(('active'), default=False)
	comment_by = models.CharField(max_length=200, null=True ,blank=True)
	email = models.CharField(max_length=200, null=True ,blank=True)
	likes = models.CharField(default='0', max_length=200, null=True ,blank=True)

class ArticleCommentResponse(models.Model):
	Comment = models.ForeignKey(ArticleComment, on_delete = models.CASCADE)
	response =models.TextField(null=True ,blank=True)
	publication_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_active = models.BooleanField(('active'), default=False)
	response_by = models.CharField(max_length=200, null=True ,blank=True)
	email = models.CharField(max_length=200, null=True ,blank=True)

class ArticleRating(models.Model):
	Article = models.ForeignKey(Article, on_delete = models.CASCADE)
	rating =models.TextField(null=True ,blank=True)
	publication_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_active = models.BooleanField(('active'), default=False)
	rating_by = models.CharField(max_length=200, null=True ,blank=True)
	email = models.CharField(max_length=200, null=True ,blank=True)

