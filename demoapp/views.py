from django.shortcuts import render, HttpResponse
# from
# Create your views here.
def index(requests):
	var = 'hii'
	return render(requests, 'index.html',{'var': var})
	