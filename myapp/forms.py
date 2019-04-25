#from django import forms
from django.forms import ModelForm
#from django.forms import Complaints
from . import models

class AddItems(ModelForm):
    class Meta:
        model = models.SellingItems
        fields = '__all__'
        labels = {
            "sell_title_text" :  "Name of Item",
            "sell_price" : "Price of Item",
            "sell_name" : "Name of Seller",
            "sell_username" : "Username",
            "sell_mail" : "Email ID",
            "sell_photo" : "Photo of Item",
            "sell_description" : "Description of Item"
        }
    def __init__(self, *args, **kwargs):
    # first call parent's constructor
        super(AddItems, self).__init__(*args, **kwargs)
        self.fields['sell_name'].widget.attrs['readonly'] = True
        self.fields['sell_post_date'].widget.attrs['readonly'] = True
        self.fields['sell_username'].widget.attrs['readonly'] = True
        self.fields['sell_mail'].widget.attrs['readonly'] = True
class NewAddItems(ModelForm):
    class Meta:
        model = models.SellingItems
        fields = '__all__'
        labels = {
            "sell_title_text" :  "Name of Item",
            "sell_price" : "Price of Item",
            "sell_name" : "Name of Seller",
            "sell_username" : "Username",
            "sell_mail" : "Email ID",
            "sell_photo" : "Photo of Item",
            "sell_description" : "Description of Item"
        }
    def __init__(self, *args, **kwargs):
    # first call parent's constructor
        super(NewAddItems, self).__init__(*args, **kwargs)
        self.fields['sell_post_date'].widget.attrs['readonly'] = True


class Complaint(ModelForm):
    class Meta:
        model = models.Complaints
        fields = '__all__'
        labels = {
            "sell_name" : "Name",
            "sell_username" : "Username",
            "sell_mail" : "Email ID",
            "sell_description" : "Description of Complaint"
        }
    def __init__(self, *args, **kwargs):
    # first call parent's constructor
        super(Complaint, self).__init__(*args, **kwargs)
        