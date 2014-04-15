from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	# username, first_name, last_name, email, and password added through
	# abstractbaseuser
	school = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)
	grad_year = models.CharField(max_length=200)
	major = models.CharField(max_length=200)
	# add file field for resume

	def __str__(self):
		return "%s -%s -%s" % (self.username, self.first_name, self.last_name)

class Rating(models.Model):
	rated = models.ForeignKey(User, related_name="rated")
	rater = models.ForeignKey(User, related_name="rater")
	rating = models.IntegerField()

	def __str__(self):
		return "rated: %s , rater: %s, rating: %s" % (self.rated.username, self.rater.username, str(self.rating))
class Skill(models.Model):
	skill = models.CharField(max_length=200)

	def __str__(self):
		return self.skill

class hasSkill(models.Model):
	user = models.ForeignKey(User)
	skill = models.ForeignKey(Skill)

	def __str__(self):
		return "%s - %s" % (self.user.username, self.skill.skill)
class Experience(models.Model):
	title = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)

	def __str__(self):
		return "%s - %s" % (self.title, self.company)
 
class hasExperience(models.Model):
	user = models.ForeignKey(User)
	experience = models.ForeignKey(Experience)

	def __str__(self):
		return "%s - %s" %(self.user.username, self.experience.title)
