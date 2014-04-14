from django.db import models

class User(models.Model):
	username = models.IntegerField()
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	password_description = models.CharField(max_length=200)
	grad_year = models.CharField(max_length=200)
	major = models.CharField(max_length=200)
	# add file field for resume

class Ratings(models.Model):
	rated = models.ForeignKey(User, related_name="rated")
	rater = models.ForeignKey(User, related_name="rater")
	start = models.IntegerField()
class Skill(models.Model):
	skill = models.CharField(max_length=200)

class hasSkill(models.Model):
	user = models.ForeignKey(User)
	skill = models.ForeignKey(Skill)
class Experience(models.Model):
	title = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
 
class hasExperience(models.Model):
	user = models.ForeignKey(User)
	Experience = models.ForeignKey(Experience)