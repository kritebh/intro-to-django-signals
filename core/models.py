from django.db import models
from django.db.models.signals import pre_save,post_save  #Inbuilt Signals
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

def save_post(sender,instance,**kwargs):
    print("Pre save")

pre_save.connect(save_post,sender=Post) # This will trigger after the saving data into Post model
