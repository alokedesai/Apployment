from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	username = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
 	last_name = models.CharField(max_length=200)
 	email = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	school_location = models.CharField(max_length=200)
	school_type = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)
	grad_year = models.CharField(max_length=200)
	major = models.CharField(max_length=200)
	resume = models.FileField(blank=True, null=True, upload_to="resume")
	gpa = models.FloatField(blank=True, null=True)
	stars = models.IntegerField(blank = True, null=True)
	wage = models.IntegerField(blank=True, null=True)
	rank = models.IntegerField(blank=True, null=True)

	# information necessary for extending abstractbaseuser
	USERNAME_FIELD = "username"
	REQUIRED_FIELDS=["email", "first_name", "last_name", "school", "grad_year"]
	def __str__(self):
		return "%s -%s -%s" % (self.username(), self.first_name, self.last_name)

class Review(models.Model):
	rated = models.ForeignKey(User, related_name="rated")
	rater = models.ForeignKey(User, related_name="rater")
	text = models.TextField()
	stars = models.IntegerField()

	def __str__(self):
		return "rated: %s , rater: %s, stars: %s" % (self.rated.username, self.rater.username, str(self.stars))

class Skill(models.Model):
	skill = models.CharField(max_length=200)

	def __str__(self):
		return self.skill

class hasSkill(models.Model):
	user = models.ForeignKey(User)
	skill = models.ForeignKey(Skill)

	def __str__(self):
		return "%s - %s" % (self.user.username, self.skill.skill)
 
class hasExperience(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)

	def __str__(self):
		return "%s - %s" %(self.user.username, self.title.title)
