from django.db import models
from sacco.models import Article, Objective, NationalStaffMember
from users.models import AccountUser
# Create your models here.
class HomePage(models.Model):
	logo = models.ImageField(null=True ,blank=True, upload_to='media/images')
	mission =models.TextField(null=True ,blank=True)
	def __str__(self):
		return self.mission
class HomePageSlider(models.Model):
	home_page = models.ForeignKey(HomePage, on_delete = models.CASCADE,null=True ,blank=True,default=None)

	image = models.ImageField(null=True ,blank=True, upload_to='media/images')
	title =models.TextField(null=True ,blank=True)
	sub_title1 =models.TextField(null=True ,blank=True)
	sub_title2 =models.TextField(null=True ,blank=True)
	def __str__(self):
		return self.title

class Facts(models.Model):
	video_url = models.TextField(null=True ,blank=True)
	image = models.ImageField(null=True ,blank=True, upload_to='media/images')
	title =models.TextField(null=True ,blank=True)
	text =models.TextField(null=True ,blank=True)
	def __str__(self):
		return self.title

class Testimonial(models.Model):
	profile = models.ForeignKey(AccountUser, on_delete = models.CASCADE,null=True ,blank=True,default=None)
	video_url = models.TextField(null=True ,blank=True)
	image = models.ImageField(null=True ,blank=True, upload_to='media/images')
	title =models.TextField(null=True ,blank=True)
	text =models.TextField(null=True ,blank=True)
	def __str__(self):
		return self.title
class HomePageFacts(models.Model):
	home_page = models.ForeignKey(HomePage, on_delete = models.CASCADE,null=True ,blank=True,default=None)
	facts = models.ForeignKey(Facts, on_delete = models.CASCADE, null=True ,blank=True)
	def __str__(self):
		return self.facts.title
class HomePageTestimonial(models.Model):
	home_page = models.ForeignKey(HomePage, on_delete = models.CASCADE,null=True ,blank=True,default=None)

	testimonial = models.ForeignKey(Testimonial, on_delete = models.CASCADE, null=True ,blank=True,default=None)
	def __str__(self):
		return self.testimonial.title
class HomePageArticle(models.Model):
	home_page = models.ForeignKey(HomePage, on_delete = models.CASCADE,null=True ,blank=True,default=None)

	article = models.ForeignKey(Article, on_delete = models.CASCADE, null=True ,blank=True,default=None)

	def __str__(self):
		return self.article.title

class HomePageObjective(models.Model):
	home_page = models.ForeignKey(HomePage, on_delete = models.CASCADE,null=True ,blank=True,default=None)

	video_url = models.TextField(null=True ,blank=True)
	objective = models.ManyToManyField(Objective)
	video_title =models.TextField(null=True ,blank=True)
	video_subtitle =models.TextField(null=True ,blank=True)

	def __str__(self):
		return self.objective.title
# class AboutUs(models.Model):
#     logo = models.ImageField(null=True ,blank=True, upload_to='media/images')
#     mission =models.TextField(null=True ,blank=True)
#     def __str__(self):
#         return self.user.first_name

# class JoinUs(models.Model):
#     logo = models.ImageField(null=True ,blank=True, upload_to='media/images')
#     mission =models.TextField(null=True ,blank=True)


# class OurMembers(models.Model):
#     logo = models.ImageField(null=True ,blank=True, upload_to='media/images')
#     mission =models.TextField(null=True ,blank=True)
#     def __str__(self):
#         return self.user.first_name

class BoardMembers(models.Model):
	staff = models.ForeignKey(NationalStaffMember, on_delete = models.CASCADE,null=True ,blank=True,default=None)
	board_statement =models.TextField(null=True ,blank=True)
	# mission =models.TextField(null=True ,blank=True)
	def __str__(self):
		return self.user.first_name

