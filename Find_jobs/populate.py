import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Find_jobs.settings')
import django
django.setup()


from faker import Faker # type: ignore
from random import *
from testapp.models import Hyderabad_jobs
from testapp.models import Banglore_jobs
from testapp.models import Pune_jobs

fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num += str(randint(0,9))

    return int(num)    

# def populate(n):
#     for i in range(n):
#         fdate=fake.date()
#         fcompany=fake.company()
#         ftitle=fake.random_element(elements=('project Manager','Team Lead','software Engineer','HR','Associate Engineer'))
#         faddress=fake.address()
#         femail=fake.email()
#         fphonenumber=phonenumbergen()

#         Hyd_jobs_record= Hyderabad_jobs.objects.get_or_create(
#             date=fdate,
#             company=fcompany,
#             title=ftitle,
#             address=faddress,
#             email=femail,
#             phonenumber=fphonenumber,
           

#         )


# def populate(n):
#     for i in range(n):
#         fdate=fake.date()
#         fcompany=fake.company()
#         ftitle=fake.random_element(elements=('project Manager','Team Lead','software Engineer','HR','Associate Engineer'))
#         faddress=fake.address()
#         femail=fake.email()
#         fphonenumber=phonenumbergen()

#         Banglore_jobs_record= Banglore_jobs.objects.get_or_create(
#             date=fdate,
#             company=fcompany,
#             title=ftitle,
#             address=faddress,
#             email=femail,
#             phonenumber=fphonenumber,
           

#         )   


def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project Manager','Team Lead','software Engineer','HR','Associate Engineer'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()

        Pune_jobs_record= Pune_jobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
           

        )              

n=int(input('Enter number of records:'))
populate(n)

print(f'{n} reconrd  inserted sucessfully')