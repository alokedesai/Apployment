from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from apployment_site.models import *
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from apployment_site.forms import DocumentForm

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
                resume = request.FILES["file"]

                # Experience attributes
                title = request.POST.get("title1")
                company = request.POST.get("company1")
                co_description = request.POST.get("expDescription1")

                # make sure no user exists with this username or email
                if User.objects.filter(username=theUser) or User.objects.filter(email=email):
                        return HttpResponse("Error!")
                # create corresponding user, and skill objects
                user = User(username=theUser, email = email, first_name=first_name, last_name=last_name, school=school,grad_year=year,major=major, description=description, resume=resume)                
                user.set_password(password)
                user.save()
                for s in skill:
                        y = hasSkill(user =user, skill=Skill.objects.filter(skill=s)[0])
                        y.save()
                # create the experience
                E = Experience(title=title, company=company, description=co_description)
                E.save()

                y = hasExperience(user=user, experience=E)
                y.save()

                user= authenticate(username=theUser, password=password)
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
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(request.user.email.lower()).hexdigest()
        gravatar_url += "?" + "s=150" +"&" + "d=" + "mm"

        # return the first experience 
        exp = hasExperience.objects.filter(user__username=request.user.username)[0]
        return render(request, "apployment_site/profile.html", {"skills" : skills, "stars":stars, "image": gravatar_url, "exp" : exp.experience})

def search(request):
        if request.method == "POST":
                # get the school
                school = request.POST.get("school")
                skills = request.POST.getlist('skills')
                
                # really complex query, think of how to simplify!
                school = hasSkill.objects.filter(user__school__contains=school)
                skill = school.filter(skill__skill__in=skills).values("user").distinct()

                result = []
                for developer in skill:
                        result.append(User.objects.get(id=developer["user"]))

                return render(request, "apployment_site/search.html", {"skills" : skills, "result": result})
        skills = Skill.objects.all()
        return render(request, "apployment_site/search.html", {"skills" : skills})
def user(request, username):
        user = User.objects.filter(username=username)
        if not user:
                return HttpResponse("404")
        user = user[0]
        skills = hasSkill.objects.filter(user__username=user.username)
        rating = Review.objects.filter(rated__username=user.username)

        stars = None
        if rating:
                stars = rating[0].stars
        # gravatar URL
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(user.email.lower()).hexdigest()
        gravatar_url += "?" + "s=150" +"&" + "d=" + "mm"
        notcurrent = (request.user != user)
        return render(request, "apployment_site/profile.html", {"skills" : skills, "stars":stars, "user" : user, "image" : gravatar_url, "notcurrent" : notcurrent})
@login_required
def rate(request, rated):
        rated= User.objects.filter(username = rated)
        if not rated or request.user.username == rated[0]:
                return HttpResponse("404")
        rated = rated[0]

        if request.method == "POST":
                # get current user
                current_user = request.user
                stars = None
                try:
                        stars = int(request.POST.get("skills"))
                except:
                        return HttpResponse("please enter a value for the stars")
                text = request.POST.get("description")
                r = Review(rated=rated, rater=current_user, stars=stars, text=text)
                r.save()
                return redirect("/user/" + rated.username)



        return render(request, "apployment_site/rate.html", {"rated" : rated})