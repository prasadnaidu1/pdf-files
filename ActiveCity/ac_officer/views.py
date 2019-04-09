from django.shortcuts import render

# Create your views here.
def officerComplaint(request):
    return render(request,"ac_officer/officer_complaint.html")