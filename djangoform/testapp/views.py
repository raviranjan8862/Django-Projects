from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.
def studentinput_view(request):
  
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            print ('form validation sucess and print data')
            print('Rollno:', form.cleaned_data['rollno'])
            print('Name:', form.cleaned_data['name'])
            print('Marks:', form.cleaned_data['marks'])
            sname=form.cleaned_data['name']
            submitted=True

    form=StudentForm()        
    # my_dict={'form':form}
    return render(request, 'testapp/input.html',{'form':form,'sname':sname,'submitted':submitted})
