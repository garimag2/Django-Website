# Create your views here.
from django.shortcuts import render, get_object_or_404, reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import SellingItems, Complaints
import operator
from django.contrib.auth.models import User                               
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Message                                                   
from myapp.serializers import MessageSerializer, UserSerializer 
from .forms import AddItems, NewAddItems, Complaint

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    #context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': "I am bold font from the context"}
    #if request.user.is_authenticated:
        selling_list = SellingItems.objects.order_by('sell_name')[:5]
        context_dict = {'selling_items': selling_list}
        print(context_dict)
        # Return a rendered response to send to the client.
        # We make use of the shortcut function to make our lives easier.
        # Note that the first parameter is the template we wish to use.

        return render(request, 'home.html', context_dict)
    #return render_to_response('home.html', context_dict, context)
    #if request.method == 'GET':
    #    return render(request, 'chat_view', {})
    #if request.method == "POST": #Authentication of user
    #    return redirect('message_view')

def search_value(request):
    questions=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        print(search)
        questions = SellingItems.objects.filter(sell_title_text__icontains=search)

    return render(request, 'home.html',{'selling_items': questions})

def selling_item_detail(request,id):
    post = get_object_or_404(SellingItems, id=id)
    print(post)
    return render(request, 'description.html', {'selling_items': post})


    #return HttpResponseRedirect(reverse('description.html'))
    #return render(request, 'message.html', {'user': User})
def chat_view(request):
    """Render the template with required context variables"""
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        return render(request, 'message.html',
                      {'users': User.objects.exclude(username=request.user.username)})

def message_view(request, sender, receiver): 
    """Render the template with required context variables"""
    #receiver = User.objects.filter(username=name_seller).values_list('id', flat=True)[0]
    #post = get_object_or_404(SellingItems, id=id)
    #sender = User.objects.filter(username=name_user).values_list('id', flat=True)[0]
    print(sender)
    print(receiver)
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        #print(request.user.username)
        return render(request, "chat.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)}) 
# Users View

def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if pk:                                                                      # If PrimaryKey (id) of the user is specified in the url
            users = User.objects.filter(id=pk)              # Select only that particular user
        else:
            users = User.objects.all()                             # Else get all user list
        serializer = UserSerializer(users, many=True, context={'request': request}) 
        return JsonResponse(serializer.data, safe=False)               # Return serialized data
    elif request.method == 'POST':
        data = JSONParser().parse(request)           # On POST, parse the request object to obtain the data in json
        serializer = UserSerializer(data=data)        # Seraialize the data
        if serializer.is_valid():
            serializer.save()                                            # Save it if valid
            return JsonResponse(serializer.data, status=201)     # Return back the data on success
        return JsonResponse(serializer.errors, status=400)     # Return back the errors  if not valid

@csrf_exempt
def message_page(request,sender = None,receiver = None):
    #receiver = User.objects.filter(username=name_seller).values_list('id', flat=True)[0]
    #post = get_object_or_404(SellingItems, id=id)
    #sender = User.objects.filter(username=name_user).values_list('id', flat=True)[0]
    #print(seller_id)
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        #print(messages)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        #print(serializer)
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        #print("Helllllooooo ******************")
        #print(data)
        #print("-------------------------------")
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def add_view(request):
    if request.method == 'POST':
        form = NewAddItems(request.POST, request.FILES)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("Hi")
            return redirect('home')
    else:
        form = NewAddItems()
    return render(request, 'submit_new_form.html',{'form': form})

@csrf_exempt
def add_edit_items(request, sell_id):
    # if this is a POST request we need to process the form data
    instance = get_object_or_404(SellingItems, id=sell_id)
    if request.method == 'POST':
        form = AddItems(data = request.POST or None, files = request.FILES or None, instance = instance)
        #model_form = MyModelUpdateForm(POST, instance=myModelobject )
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            print("Hi")
            return redirect('home')    
    # if a GET (or any other method) we'll create a blank form
    else:
        #instance = get_object_or_404(SellingItems, id=sell_id)
        form = AddItems(instance= instance)
        print("Hi1")

    return render(request, 'submit_form.html',
                      {'selling_items' : SellingItems.objects.get(id = sell_id), 'form' : form})

def add_complaint(request):
    if request.method == 'POST':
        form = Complaint(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            print("Hi")
            return redirect('query_submitted')   
    # if a GET (or any other method) we'll create a blank form
    else:
        #instance = get_object_or_404(SellingItems, id=sell_id)
        form = Complaint()
        print("Hi1")

    return render(request, 'complaint_form.html',{'form' : form})