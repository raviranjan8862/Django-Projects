from django.shortcuts import render
import datetime

# Create your views here.
def Home(request):
    date=datetime.datetime.now()
    coursename='Django'
    Prerequisite='Python'
    g1='Good to get job very easily'
    g2='Learning is also very easy'
    g3='You can claim 3 to 4 years of exp'
    g4='It is very helpful for fresher'

    my_dict={'insert_date':date,'coursename':coursename,'Prerequisite':Prerequisite,'g1':g1,'g2':g2,'g3':g3,'g4':g4,}

    return render(request, 'testapp/home.html', context=my_dict)
