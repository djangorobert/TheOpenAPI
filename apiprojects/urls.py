"""apiprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#Lets use a TemplateView to bring in our React Index.html

from django.views.generic import TemplateView
from rest_framework import routers
from blog import views

#Impor your Player APP views here



#this is for STATIC
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
#router.register(r'game', views.GameViewSet)
#router.register(r'players', views.PlayerViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
<<<<<<< HEAD
    path('home', views.home, name='home'),
    path('users', views.get_users, name='get_users'),

    path('api/', include(router.urls)),
=======
    path('', include(router.urls)),
>>>>>>> a76c098a2995ead186bb062d4aafc38a3ef9ce78
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='blog/index.html')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
