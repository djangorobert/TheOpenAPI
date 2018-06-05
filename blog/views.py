from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.serializers import UserSerializer, PostSerializer, PointsSerializer, GameSerializer, PlayerSerializer
from blog.models import Post
#Lets import our Player APP
#Importing Request Module for api request
<<<<<<< HEAD
import requests
#to get Json data in a list for django do this
from django.http import JsonResponse
#Lets Add in some Django Rest Framework imports



=======
>>>>>>> a76c098a2995ead186bb062d4aafc38a3ef9ce78


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

<<<<<<< HEAD


#Lets import our Player APP
from player.models import Points, Game, Player


class PointsViewSet(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer





class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer



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


=======
>>>>>>> a76c098a2995ead186bb062d4aafc38a3ef9ce78
