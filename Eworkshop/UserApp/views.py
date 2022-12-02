from django.shortcuts import render,redirect
from .models import User,insurance
from rest_framework.decorators import api_view,permission_classes
from math import sin, cos, sqrt, atan2, radians
import reverse_geocoder as rg
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from .serializers import UserSerializer, insuranceSerializer
from rest_framework.authtoken.views  import ObtainAuthToken
from  rest_framework.authtoken.models import Token
import reverse_geocoder as rg
# from django.core.files.storage import FileSystemStorage
import base64
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile

# Create your views here.

def home(request):
    return render(request,"login.html")


def listmechanic(request):
    me=User.objects.filter(role="mechanic",is_approved="disapproved").values()
    return render(request,"mechaniclist.html",{'me':me})

def listinsurance(request):
    ins=insurance.objects.filter(status="requested")
    return render(request,"insurance.html",{'ins':ins})

def updateinsurance(request,insuranceid):
    k=insurance.objects.filter(id=insuranceid).values()
    print(k[0])
    if request.method=="POST":
        owner=request.POST.get('owner')
        vehicle_no=request.POST.get('vehicle_no')
        vehicle_type=request.POST.get('vehicle_type')
        vehicle_model=request.POST.get('vehicle_model')
        house_name=request.POST.get('house_name')
        place=request.POST.get('place')
        status="renewed"
        issue_date=request.POST.get('issue_date')
        expiry_date=request.POST.get('expiry_date')
        k.update(owner=owner,vehicle_no=vehicle_no,vehicle_type=vehicle_type,status=status,vehicle_model=vehicle_model,house_name=house_name,place=place,issue_date=issue_date,expiry_date=expiry_date)
        # return redirect('updateinsurance')
    return render(request,"updateins.html",{"k":k[0],"id":insuranceid})

def deletemechanic(request,userid):
    me=User.objects.get(id=userid)
    me.delete()
    return render(request,"index.html")

def deleteinsurance(request,insuranceid):
    me=insurance.objects.get(id=insuranceid)
    me.delete()
    return render(request,"index.html")


def approve(request,userid):
    ap=User.objects.get(id=userid)
    ap.is_approved="approved"
    ap.save()
    return redirect('')

# def deleteapprove(request,userid):
#     ap=User.objects.get(id=userid)
#     ap.delete()
#     return render(request,"index.html")


def adminlogin(request):
    if request.method == 'POST':
        email=request.POST.get('mail')
        password=request.POST.get('password')
        if email=="akshay779966@gmail.com" and password=="akshay":
            return render(request,"index.html")
        else:
            messege=" Sorry Invalid Username Or Password"
            return render(request,"login.html",{'messege':messege})
    return render(request,"login.html")

