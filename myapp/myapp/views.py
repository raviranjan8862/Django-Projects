from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):
  
    if request.method=='POST':
     check=request.POST['check']
     print(check)

    date=datetime.datetime.now()
    isActive=True
    name="Ravi ranjan"
    list_of_fruits=[
        'Apple',
        'Banana',
        'Mango',
    ]

    student={
       'student_name':"Ravi ranjan",
       'student_Eno':"03121202022",
       'student_course':"BCA",

    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'fruits':list_of_fruits,
        'student_data':student,

    }


    return render(request,"home.html",data)

def about(request):
    date=datetime.datetime.now()
    print(" test function is called from view")
    return render(request,"about.html",{})

def service(request):
    date=datetime.datetime.now()
    print(" test function is called from view")
    return render(request,"service.html",{})