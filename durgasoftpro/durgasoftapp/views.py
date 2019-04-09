from django.shortcuts import render
from .models import ContactData, FeedbackData
from .forms import ContactForm, FeedbackForm

def home(request):
    return render(request,'durgahome.html')


def services(request):
    return render(request,'durgaservices.html')


def contact(request):
    if request.method =="POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            fname = request.POST.get('firstname','')
            lname = request.POST.get('lastname','')
            email = request.POST.get('email','')
            mobile = request.POST.get('mobile','')

            data  = ContactData(
                firstname=fname,
                lastname=lname,
                email=email,
                mobile=mobile
            )
            data.save()
            cform = ContactForm()
            return render(request,'durgacontact.html',{'cform':cform})


    else:
        cform = ContactForm()
        return render(request, 'durgacontact.html',{'cform':cform})

import  datetime
time1 = datetime.datetime.now()

def feedback(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating','')
            feedback = request.POST.get('feedback','')

            name = name.capitalize()

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                time=time1
            )
            data.save()
            fform = FeedbackForm()
            return render(request,'durgafeedback.html',{'fform':fform})


    else:
        fbdata = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request,'durgafeedback.html',{'fform':fform, 'fbdata':fbdata})


def gallery(request):
    return render(request,'durgagallery.html')









