from django.dispatch.dispatcher import receiver
from django.shortcuts import render,HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver,Signal
from .models import Post
# Create your views here.
time_stamp = Signal(providing_args=['timestamp'])
def home(request):
    time_stamp.send(sender=Post,timestamp="30/05/2021")
    return HttpResponse("Home Page")

## Inbuilt Signal
@receiver(request_finished)
def track(sender,**kwargs):
    print("Finished")

## Custom Signal
@receiver(time_stamp)
def own_track(sender,**kwargs):
    print(kwargs)