from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "chat/home.html", {})


def room(request, label):
    room = Room.objects.get_or_create(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    context = {
        'room': room,
        'messages': messages
    }
    return render(request, "chat/room.html", context)
