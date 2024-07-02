from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(label='Enter password',widget=forms.PasswordInput)
    rpassword=forms.CharField(label='password(Again)', widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False, widget=forms.HiddenInput)



    def clean(self):
      print('total form vali(dations....')
      total_cleaned_data=super().clean()
      print('validating name')
      inputname=total_cleaned_data['name']
      if inputname[0].lower() !='s':
         raise forms.ValidationError('name should start with s')
      print('validatin rollno')
      inputrollno=total_cleaned_data['rollno']
      if inputrollno<=0:
         raise forms.ValidationError('roll no should be > 0')
      print('validation of email')
      inputemail=total_cleaned_data['email']
      if inputemail[-10:] !='@gmail.com':
         raise forms.ValidationError('Email should contain be @gmail.com')
      print('password validation')
      pwd=total_cleaned_data['password']
      rpwd=total_cleaned_data['rpassword']
      if pwd !=rpwd:
         raise forms.ValidationError('both password must be same.......')
      
      bot_handler_value=total_cleaned_data['bot_handler']
      if len(bot_handler_value) <0:
        raise forms.ValidationError('request from bot ... cant submitted')
      
      print("feedback validation")
      inputfeed=total_cleaned_data['feedback']
      if len(inputfeed) <10:
         raise forms.ValidationError('please provid descriptive feedback.....')
      
      
      
      
    


    #By using django in-built validators
    # feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])


    # Explicitly by the porgramer by using clean method
    # def clean_name(self):
    #     print('validating the name field')
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError('The minium number of character in the name field should be 4')
    #     return inputname

    # def clean_rollno(self):
    #     print('Validating rollno field')
    #     inputrollno=self.cleaned_data['rollno']
    #     return inputrollno
    # def clean_email(self):
    #     print('validation email field')
    #     inputemail=self.cleaned_data['email']
    #     return inputemail
    
    # def clean_feedback(self):
    #     print("validating feedback field")
    #     inputfeedback=self.cleaned_data['feedback']
    #     return inputfeedback
    
