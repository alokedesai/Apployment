
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from apployment_site.models import *
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import urllib, hashlib

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

                # Experience attributes
                title = request.POST.get("title1")
                company = request.POST.get("company1")
                description = request.POST.get("expDescription1")

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
                user= authenticate(username=username, password=password)
                login(request, user)
                return redirect("/")
               

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
@login_required
def profile(request):
        skills = hasSkill.objects.filter(user__username=request.user.username)
        rating = Review.objects.filter(rated__username=request.user.username)
        stars = None
        if rating:
                stars = rating.stars
        return render(request, "apployment_site/profile.html", {"skills" : skills, "stars":stars})

def search(request):
        if request.method == "POST":
                # get the school
                school = request.POST.get("school")
                skills = request.POST.getlist('skills')
                
                # really complex query, think of how to simplify!
                result = hasSkills.objects.filter(user__school_contains=school)
                fresult = result.filter(skill__skill__in=skills)

        skills = Skill.objects.all()
        return render(request, "apployment_site/search.html", {"skills" : skills})

