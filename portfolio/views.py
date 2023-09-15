from django.shortcuts import render,HttpResponse
from datetime import datetime
from portfolio.models import Contact

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact=Contact(name=name,number=number,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
        return HttpResponse('Submitted')
    return render(request,'index.html')
