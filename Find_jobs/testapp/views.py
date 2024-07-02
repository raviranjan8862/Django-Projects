from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'testapp/index.html',)

from testapp.models import Hyderabad_jobs
def hydjobs_views(request):
    jobs_list=Hyderabad_jobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request, 'testapp/hydjobs.html', my_dict)

from testapp.models import Banglore_jobs
def Bangjobs_views(request):
    jobs_list=Banglore_jobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request, 'testapp/Bangjobs.html', my_dict)


from testapp.models import Pune_jobs
def Punejobs_views(request):
    jobs_list=Pune_jobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request, 'testapp/punejobs.html', my_dict)