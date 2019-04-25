from django.db import models
from django.contrib.auth.models import User
import datetime
#from django.contrib.auth.models import AbstractUser
# Create your models here.

class SellingItems(models.Model):
    sell_title_text = models.CharField(max_length=200)
    sell_post_date = models.DateTimeField('date published', default = datetime.datetime.now())
    sell_price = models.IntegerField()
    sell_name = models.CharField(max_length = 50)
    sell_username = models.CharField(max_length = 50)
    sell_mail = models.CharField(max_length = 50)
    sell_photo = models.ImageField(upload_to = 'pic_folder/', default = '')
    sell_description = models.TextField(max_length=1000)
 
class Message(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default=False)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('timestamp',)

class Complaints(models.Model):
      sell_name = models.CharField(max_length = 50)
      sell_username = models.CharField(max_length = 50)
      sell_mail = models.CharField(max_length = 50)
      sell_description = models.TextField(max_length=1000)