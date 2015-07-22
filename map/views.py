from django.shortcuts import render
 
def PageWithJquery( request ):
	return render( 'home.html')
# Create your views here.
def index(request):
	return render(request, "index.html")
def generic(request):
    return render(request, "generic.html")
def elements(request):
    return render(request, "elements.html")