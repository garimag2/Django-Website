# Register your models here.
#from django.contrib import admin
from django.contrib import admin

from .models import SellingItems
from .models import Message
from .models import Complaints

admin.site.register(Message)
admin.site.register(SellingItems)
admin.site.register(Complaints)
