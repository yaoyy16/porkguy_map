from django.shortcuts import render
 
def PageWithJquery( request ):
    return render( 'home.html',
            {"mytitle":"customize_title"})
# Create your views here.
def home(request):
    return render(request, "home.html")