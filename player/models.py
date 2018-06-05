from django.db import models
# Lets Create our Managers
from django.db.models import Avg
class NameManager(models.Manager):
    def get_queryset(self):
        return super(NameManager, self).get_queryset().filter(name='Lebron')



# Create your models here.
# A Model to create a Player
class Player(models.Model):
    CAVALIERS = 'Cleveland Cavaliers'
    WARRIORS = 'Golden State Warriors'
    BOSTON = 'Boston Celtics'
    HOUSTON = 'Houson Rockets'

    TEAM = (
        (CAVALIERS, 'Cleveland Cavaliers'),
        (WARRIORS, 'Golden State Warriors'),
        (BOSTON, 'Boston Celtics'),
        (HOUSTON, 'Houston Rockets'),
    )

    name = models.CharField(max_length=30)
    team = models.CharField(
        max_length=30,
        choices=TEAM)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Points(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    points = models.DecimalField(max_digits=6, decimal_places=2)
    assists = models.DecimalField(max_digits=6, decimal_places=2)
    #points_manager = PointsManager()

    def __str__(self):
        return str(self.points)

class Game(models.Model):
    GAME1 = 'Game1'
    GAME2 = 'Game2'
    GAME3 = 'Game3'
    GAME4 = 'Game4'
    GAME5 = 'Game5'
    GAME6 = 'Game6'
    GAME7 = 'Game7'

    GAMES = (
        (GAME1, 'Game1'),
        (GAME2, 'Game2'),
        (GAME3, 'Game3'),
        (GAME4, 'Game4'),
        (GAME5, 'Game5'),
        (GAME6, 'Game6'),
        (GAME7, 'Game7'),
    )

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.ForeignKey(Points, on_delete=models.CASCADE)
    game = models.CharField(
        max_length=30,
        choices=GAMES)

    def __str__(self):
        return str(self.player)

