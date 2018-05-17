# TheOpenAPI
A Django Rest Framework API built to show a free API with a django Model


#STEPS To get started
#If you do not have virtualenv installed you can by running this command
pip install virtualenv
#once you have that run this command to get started

virtualenv exampleenv
cd exampleenv

# Make sure to activate the virtualenv
source bin/activate 
or scripts.\activate
#now install django
pip install django

#Install django rest framework with pip 
pip install djangorestframework

#add restframework in the settings.py here in a minute 

#Now lets create a django project
django-admin startproject djanogproject

#cd into it
cd djangoproject
 
#Run the migrations 
python manage.py makemigrations

# Run migrate next
python manage.py migrate

#Lets create a superuser so that once the site is up and running we can log into the FREE Django Admin
python manage.py createsuperuser

#Check to see if the development server launches successfully

python manage.py runserver

#you should get a succesful run go to 127.0.0.:8000 or you can also type in localhost in your browser.

#Next we want to create a APP it can be whatever depending on the data you want _to get or app you want
python manage.py startapp blog

# next you will make sure to add blog in the settings.py file 
Add it under installed apps
blog

#also make sure that restframework is add there as well 
rest_framework


#Next thing you want to do is create your URLS

#While your there add in the Routers , routers are coming from Django REST framework they are like urls they communicate with your 
serializers and the serializers will be our views for the API.

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from blog import views
#this is for STATIC
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# next lets build the serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'author', 'title', 'text')
        

# next lets create the views.py file

from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.serializers import UserSerializer, PostSerializer
from blog.models import Post

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
    
    
    
 #thats it make sure to run the runserver commmand 
 python manage.py runserver
 
 #Now go back to localhost on your broswer
 
 #To create data go to 127.0.0.:8000/admin and login with your creatsuperuser credentials
 
 and create a blog
it is in the admin were you can create your posts 
then when you go back to your api you will be able to see the posts in the api at the domain 127.0.0.1:8000 or localhost 

#Great you have a API up and running Next you can USE the PYTHON module Requests to consume your own API go try it.
