from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from django.utils.text import slugify
from django import forms
# Create your views here.

@login_required
def createrooms(request):
    if request.method=='POST':
        name=request.POST['creator']
        slug = slugify(name)
        f=Room(name=name, slug=slug)
        if name=='':
            return render(request, 'room/rooms.html',{'err':True})
        for instance in Room.objects.all():
            if instance.name==name:
                return render(request, 'room/rooms.html',{'error':True})
        else:
            f.save()
            return redirect('rooms')

@login_required
def rooms(request):
    rooms=Room.objects.all()
    return render(request,'room/rooms.html',{
        'rooms':rooms
    })

@login_required
def room(request, slug):
    room=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)[0:25]
    return render(request, 'room/room.html',{'room':room,
    'messages':messages
    })