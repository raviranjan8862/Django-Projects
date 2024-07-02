from django.shortcuts import render
import datetime
import random
# Create your views here.
def result_view(request):
    time=datetime.datetime.now()
    names_list=['ravi','ranjan','kumar','Nitish']
    msg_list=[
        'The golden days ahead',
        'Better to sleep more time in class',
        'Tommorow is the perfect day to propose ur GF',
        'Very soon you will get job',
        'very soon u will get Marriage ...'

    ]
    h=int( time.strftime('%H'))
    if h<12:
        s="Good morning"
    elif h<16:
            s="Good AfterNoon"

    elif h<21:
         s="Good Evening"
    else:
         s="Good Night" 

    name=random.choice(names_list) 
    msg=random.choice(msg_list)
    my_dict={'Time':time, 'Name':name, 'Message':msg, 'Wish':s}                
    return render(request, 'testapp/astrology.html', my_dict)