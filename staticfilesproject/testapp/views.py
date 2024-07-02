from django.shortcuts import render

# Create your views here.
def display(request):
    names={
        'name1':'Ravi',
        'name2':'Ranjan',
         'name3':'Kumar',
        
    }
       
    
    return render(request,'testapp/results.html', context=names)
