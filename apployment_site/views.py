from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from apployment_site.models import *

def index(request):
	return render(request, "apployment_site/index.html")

def signup(request):
	options = Skill.objects.all()
	return render(request, "apployment_site/signup.html", {"options" : options})