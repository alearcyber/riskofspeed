

from django.shortcuts import render
from django.http import HttpResponse
from .models import Run, User

def home(request):
    top_runs_list = Run.objects.order_by('time')[:]
    top_runs_list.reverse()

    context = {
        'top_runs_list': top_runs_list,
    }

    return render(request, 'speedrun/home.html', context)
