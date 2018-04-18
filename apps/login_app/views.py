from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index ( request ):
	#this is coming from project urls and going to localhost
	print "index route is working"
	return render( request, "login_app/index.html")

def login(request):
	pass

# def index(request):
#     if 'counter' not in request.session:
#         request.session['counter'] = 0
#     request.session['counter'] += 1
#     request.session['random_word'] = get_random_string(length = 14)

#     return render(request, "randomWord/index.html")


