from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def time_info(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='<h1> Hello guest very <h1>'
    if h<12:
        msg+='Good Morning'
        msg+='</h2>Now server time is:'+str(date)+'</h2>'
    elif h>=16: 
         msg+='Good AfterNoon'
         msg+='</h2>Now server time is:'+str(date)+'</h2>'
    elif  h<21:
         msg+='Good Evening'
         msg+='</h2>Now server time is:'+str(date)+'</h2>'
    else:
         msg+='Good Night'  
         msg+='</h2>Now server time is:'+str(date)+'</h2>'   

    return HttpResponse(msg)

