from django.urls import path, re_path
from django.views.generic.base import TemplateView
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('',TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.index , name='home'),
    re_path('search=$', views.search_value, name='search'),
    path('(<int:id>)/', views.selling_item_detail, name='selling_item_detail'),
    path('messages/api/<int:sender>/<int:receiver>/', views.message_page, name='message_page'),
    path('messages/api/',views.message_page, name='message_list'),
    path('messages/<int:sender>/<int:receiver>/', views.message_view, name='message_view'),
    path('edit/<int:sell_id>', views.add_edit_items, name='add_edit_items'),
    path('add/', views.add_view, name='add_view'),
    path('complaint/', views.add_complaint, name = 'add_complaint'),
    path('complaint/submit', TemplateView.as_view(template_name="query_submitted.html"), name='query_submitted'),
    #path('edit/add_edit_items', views.add_edit_items, name='add_edit_items'),
     # URL form : "/api/messages/1/2"
    #path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('messages/', views.chat_view, name='chat_view'),   # For POST
    # URL form "/api/users/1"
    path('api/users/<int:id>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
] 