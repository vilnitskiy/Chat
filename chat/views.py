import random
import string

from django.db import transaction
from django.shortcuts import render, redirect

from haikunator import Haikunator
from .models import Room


def home(request):
    return render(request, "chat/home.html", {})


def new_room(request):
    new_room = None
    haikunator = Haikunator()
    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(room, label=label)


def room(request, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    context = {
        'room': room,
        'messages': messages
    }
    return render(request, "chat/room.html", context)
