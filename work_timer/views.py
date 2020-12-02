from django.http import HttpResponse, HttpResponseRedirect
from .models import Timer
from django.template import loader
import datetime
import json
# Create your views here.

def index(request):
    tl = Timer.objects.all()
    timer_list = []
    for t in tl:
        print(t.__dict__)
        timer_list.append(t.__dict__)
    template = loader.get_template('work_timer/index.html')
    context = {
        'timer_list': timer_list,
    }
    return HttpResponse((template.render(context, request)))

def create(request):

    duration = datetime.time(int(request.POST['hours']), int(request.POST['minutes']), int(request.POST['seconds']))
    t = Timer(name=request.POST['name'], duration=duration)
    t.save()
    return HttpResponseRedirect("/")

def clear(request):

    print(request.POST)
    t = Timer.objects.get(pk=request.POST['id'])
    t.delete()
    return HttpResponseRedirect("/")