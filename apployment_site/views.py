
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from apployment_site.models import *
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
def index(request):
	return render(request, "apployment_site/index.html")

def signup(request):
	options = Skill.objects.all()

	if request.method == "POST":
		# get all the attributes from the form
                theUser = request.POST.get("username").lower()
                email = request.POST.get("email").lower()
                skill = request.POST.getlist('skills')
                first_name = request.POST.get("firstName")
                last_name = request.POST.get("lastName")
                school = request.POST.get("school")
                year = request.POST.get("year")
                major = request.POST.get("major")
                password = request.POST.get("password")
                description = request.POST.get("description")

                # make sure no user exists with this username or email
                if User.objects.filter(username=theUser) or User.objects.filter(email=email):
                        return HttpResponse("Error!")
                # create corresponding user, and skill objects
                user = User(username=theUser, email = email, first_name=first_name, last_name=last_name, school=school,grad_year=year,major=major, description=description)                
                user.set_password(password)
                user.save()
                for s in skill:
                        y = hasSkill(user =user, skill=Skill.objects.filter(skill=s)[0])
                        y.save()
                return HttpResponse("it worked!")

	return render(request, "apployment_site/signup.html", {"options" : options})
def signin(request):
        if request.method == "POST":
                username = request.POST.get("username").lower()
                password = request.POST.get("password").lower()
                user = authenticate(username = username, password=password)
                if user:
                        # login the user and redirect to homepage
                        login(request, user)
                        return redirect("/")

        return render(request, "apployment_site/login.html")

