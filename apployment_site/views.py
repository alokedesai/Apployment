from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from apployment_site.models import *

def index(request):
	return render(request, "apployment_site/index.html")

def signup(request):
	options = Skill.objects.all()

	if request.method == "POST":
		# get all the attributes from the form
                theUser = request.form["username"].lower()
                email = request.form["email"].lower()
                skill = request.form.getlist('skills')
                first_name = request.form["firstName"]
                last_name = request.form["lastName"]
                school = request.form["school"]
                year = request.form["year"]
                major = request.form["major"]
                password = request.form["password"]
                description = request.form["description"]

                # make sure no user exists with this username or email
                if User.objects.filter(username=theUser) or User.objects.filter(email=email):
                        return HttpResponse("Error!")
                # create corresponding user, and skill objects


	return render(request, "apployment_site/signup.html", {"options" : options})