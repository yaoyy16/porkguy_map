from django.shortcuts import render
 
def PageWithJquery( request ):
    return render( 'home.html')
# Create your views here.
def home(request):
    return render(request, "home.html")