from django.shortcuts import render
from django.http import HttpResponse

from.models import Spotlight, SocialMedia



def index(request):
    instances = Spotlight.objects.all()
    second_instances = SocialMedia.objects.all()

    context = {
        "instances":instances,
        "second_instances":second_instances,
    }

    return render(request, 'index.html', context)

