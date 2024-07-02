from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'newsapp/index.html',)


def movies_info(request):
    head_msg='Movies information'
    sub_msg1='The Pathan was nice......'
    sub_msg2='OmG will come very soon....'
    sub_msg3='Plaaning for puspha 2 with allu-arjun as lead....'
    type='movies'

    my_dict={
        'head_msg':head_msg,
        'sub_msg1':sub_msg1,
        'sub_msg2':sub_msg2,
          'sub_msg3':sub_msg3,
          'type':type
    }
    return render(request,'newsapp/news.html', my_dict)


def sports_info(request):
    head_msg='sports information'
    sub_msg1='India test team is Good......'
    sub_msg2='T20 worldcup is coming....'
    sub_msg3='Neeraj chopra is india no1 atheletes....'
    type='sports'

    my_dict={
        'head_msg':head_msg,
        'sub_msg1':sub_msg1,
        'sub_msg2':sub_msg2,
          'sub_msg3':sub_msg3,
           'type':type
    }
    return render(request,'newsapp/news.html', my_dict)


def politics_info(request):
    head_msg='politics information'
    sub_msg1='Loksabha election is going in india......'
    sub_msg2='Modi is pm of india....'
    sub_msg3='Yogi is cm of up....'
    type='politics'

    my_dict={
        'head_msg':head_msg,
        'sub_msg1':sub_msg1,
        'sub_msg2':sub_msg2,
          'sub_msg3':sub_msg3,
           'type':type
    }
    return render(request,'newsapp/news.html', my_dict)
