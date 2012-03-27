# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django import template

def home(request):
	title = " | Home"
	return render(request, "home.html", {"title" : title})
	
def contact(request):
	title = " | Contact"
	return render(request, "contact.html", {"title" : title})

def about(request):
	title = " | About"
	return render(request, "about.html", {"title" : title})
	
	

#===============================================
# Otras formas (probadas para home.

#return HttpResponse("Hello World")
	
#r = "<!DOCTYPE html> <html> <head> <title>Greeting</title> </head> <body> <p>Hello World</p> </body> </html>"
#return HttpResponse(r)
	
#tmpl = template.loader.get_template("home.html")
#return HttpResponse(tmpl.render)
#===============================================
