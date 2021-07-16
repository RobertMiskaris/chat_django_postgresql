from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message

def home(request):
    if request.user.is_authenticated:

        data = {
            'users': User.objects.all(),
        }

        if request.method == 'POST':
            if request.POST.get('search') == '':
                data['users'] = User.objects.all()
            else:
                data['users'] = User.objects.filter(username = request.POST.get('search'))

        return render(request, 'home.html', data)
    else:
        return render(request, 'title.html')


def messenger(request):
    if request.user.is_authenticated:
        return render(request, 'messenger.html')
    else:
        return render(request, 'title.html')


def message_id(request, room_id):
    if request.user.is_authenticated:
        messages = Message.objects.filter(room_id=room_id)
        return render(request, 'message.html', {'messages': messages, 'room_id': room_id})
    else:
        return render(request, 'title.html')




