import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    date=datetime.datetime.now()
    isActive=True
    name="LearnCodeWithPrakhar"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime number',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Prakhar",
        'student_college':"BIT Bangalore",
        'student_city':"Lucknow"
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)

def about(request):

    return render(request,"about.html",{})

def service(request):

    return render(request,"services.html",{})

