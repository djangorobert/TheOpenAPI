from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post
#Add in our Other APP
from player.models import Player

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'author', 'title', 'text', 'channel', 'day')

#Lets Create our Player and Points Serializer

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'name', 'team', 'age')


from player.models import Points, Game




class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('url', 'player', 'points', 'game')





class PointsSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Points
        fields = ('url', 'player', 'points')


