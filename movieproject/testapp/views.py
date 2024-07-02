from django.shortcuts import render,redirect

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

from testapp.models import Movie
def list_movies_views(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/listmovies.html',{'movie_list':movie_list})

from testapp.forms import MovieForm

def add_movie_view(request):
    form=MovieForm()
    if request.method =='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    return render(request,'testapp/addmovie.html', {'form':form})



    
