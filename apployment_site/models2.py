from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	username = models.EmailField(max_length=200)
	first_name = models.CharField(max_length=200)
 	last_name = models.CharField(max_length=200)
 	email = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)
	grad_year = models.CharField(max_length=200)
	major = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	degree_highest = models.CharField(max_length=200)
	company_name = models.CharField(max_length=200)
	rank = models.IntegerField()
	rating = models.IntegerField()
	school_type = models.CharField(max_length=200)
	gpa = models.IntegerField()
	location = models.ForeignKey(Location, related_name="location")
	company_position = models.CharField(max_length=200)
	# add file field for resume

	# information necessary for extending abstractbaseuser
	USERNAME_FIELD = "username"
	REQUIRED_FIELDS=["email", "first_name", "last_name", "school", "grad_year"]
	def __str__(self):
		return "%s -%s -%s" % (self.username(), self.first_name, self.last_name)


class Location(models.Model):
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	address = models.CharField(max_length=200)

class Reviews(models.Model):
	rated = models.ForeignKey(User, related_name="rated")
	rater = models.ForeignKey(User, related_name="rater")
	text = models.CharField(max_length=200)	
	stars = models.IntegerField()
	rater_role = models.CharField(max_length=200)	
	rated_role = models.CharField(max_length=200)	

	def __str__(self):
		return "rated: %s , rater: %s, rating: %s" % (self.rated.username, self.rater.username, str(self.stars))

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

 class File(models.Model):
	 filename = models.CharField(max_length=200)
	 
	  def __str(self):
		return "%s" % (self.filename)

class hasFile(models.Model):
	user = models.ForeignKey(User)
	filename = models.ForeignKey(File)

	def __str__(self):
		return "%s - %s" % (self.user.username, self.filename.filename)
