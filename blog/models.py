
# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    ESPN = 'ESPN'
    FOX = 'FOX'
    TNT = 'TNT'
    ABC = 'ABC'
    ESPN2 = 'ESPN2'

    CHANNEL = (
        (ESPN, 'ESPN'),
        (FOX, 'FOX'),
        (TNT, 'TNT'),
        (ABC, 'ABC'),
        (ESPN2, 'ESPN2'),
    )
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    DAY = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    )




    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    channel = models.CharField(
        max_length=5,
        choices=CHANNEL,
        null=True)
    game_date = models.DateTimeField(null=True)

    clip = models.FileField(upload_to='user_videos/', null=True)
    day = models.CharField(
        max_length=10,
        choices=DAY,
        null=True)

    created_date = models.DateTimeField(
            default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



