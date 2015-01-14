from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('Rango says hey there world! <br><a href="/rango/about">About Rango</a>')

def about(request):
	return HttpResponse('Rango says here is the about page.<br><a href="/rango">Go to Index</a>')	