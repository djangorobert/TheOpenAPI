from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.serializers import UserSerializer, PostSerializer
from blog.models import Post
#Importing Request Module for api request
import requests
#to get Json data in a list for django do this
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#Home View for the site
def home(request):
    capture = requests.get('http://www.theopenapi.info/posts/')
    c = capture.json()


    templates = 'blog/home.html'
    return render(request, templates, {'title': c[3]['title']})


def get_users(request):
    posts = Post.objects.all().values('title')
    post_list = list(posts)
    return JsonResponse(post_list, safe=False)


