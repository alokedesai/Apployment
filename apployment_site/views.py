from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def index(request):
	return render(request, "apployment_site/index.html")