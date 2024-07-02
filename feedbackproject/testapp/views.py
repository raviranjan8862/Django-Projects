from django.shortcuts import render
from testapp.forms import FeedbackForm


# Create your views here.
def feedback_view(request):
    form=FeedbackForm()
    submitted=False
    name=''
    if request.method =='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('form validation sucess and printing feedback information ')
            print('*'*55)
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('MailID:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted = True
            name = form.cleaned_data['name']

  
   
    return render(request,'testapp/feedback.html', {'form':form,'submitted':submitted,'name':name})



