from django.shortcuts import render,HttpResponse

# Create your views here
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def djcon(request):
    return render(request, 'djcon.html')

def jdcon(request):
    return render(request, 'jdcon.html')

def addContact(request):
    return render(request, 'addContact.html')