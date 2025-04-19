from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": "Wazida is a Good person"
    }
    return render(request, 'index.html',context)
    
    #return HttpResponse("this is homepage")
    
def About(request):
   # return HttpResponse("this is About US page")
   return render(request, 'About.html',)

def Services(request):
    #return HttpResponse("this is Services page")
    return render(request, 'Services.html',)

def contact(request):
    #return HttpResponse("this is contact page")
    return render(request, 'Contact.html',)


