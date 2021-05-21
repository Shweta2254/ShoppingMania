from django.shortcuts import render,HttpResponse
from website.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def offers(request):
    return render(request, 'offers.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()

    return render(request, 'contact.html')
