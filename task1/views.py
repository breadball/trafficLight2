from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests, json
from django.template import loader
from django.urls import reverse
from task1.models import *
# Create your views here.
def index(request):
    posts = post.objects.all()
    context = {'posts': posts}
    return render(request, 'template.html', context)

def load_data(request):
    users = json.loads(requests.get("http://jsonplaceholder.typicode.com/users").text)
    for user in users:
        addr = Address(street=user['address']['street'], suite=user['address']['suite'], city=user['address']['city'], zipcode=user['address']['zipcode'])
        addr.save()
        usr = User(name=user['name'], username=user['username'], email=user['email'], Address=addr, phone=user['phone'], website=user['website'])
        usr.save()
    
    posts = json.loads(requests.get("http://jsonplaceholder.typicode.com/posts").text)
    
    for pst in posts:
        user=User.objects.get(id=pst['userId'])
        data=post(user=user, title=pst['title'],body=pst['body'])
        data.save()
    post.objects.all() 
    return HttpResponseRedirect(reverse('index'))