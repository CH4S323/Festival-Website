from django.db import models

# Create your models here.

class Artist(models.Model):
    artistName = models.CharField(max_length=255)
    artistBday = models.DateField()
    artistGenere = models.CharField(max_length=255)
    artistPlatform = models.CharField(max_length=255)
    artistImage = models.ImageField(default='avatar.jpg')

    def __str__(self):
        return self.artistName


class Festival(models.Model):
    festivalName = models.CharField(max_length=255)
    festivalInfo = models.TextField()
    festivalImage = models.ImageField(default='pexels-alexander-suhorucov-6457579.jpg')
    festivalStartDate = models.DateField(null=True)
    festivalEndDate = models.DateField(null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.festivalName
    
class Event(models.Model):
    festivalName = models.ForeignKey(Festival, on_delete=models.CASCADE, null=True)
    eventName = models.CharField(max_length=255)
    eventDate = models.DateField(null=True)
    eventStart = models.CharField(max_length=20, null=True)
    eventEnd = models.CharField(max_length=20, null=True)
    artistName = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventName

class Ticket(models.Model):
    type = [
        ('early-bird', 'Early bird'),
        ('standard', 'Standard')
    ]

    ticketFullName = models.CharField(max_length=100)
    ticketEmail = models.EmailField(unique=True)
    ticketPhone = models.CharField(max_length=15)
    ticketType = models.CharField(max_length=20, choices=type)
    ticketRequest = models.TextField(null=True, blank = True)

class Message(models.Model):
    messageFullName = models.CharField(max_length=100)
    messageEmail = models.EmailField()
    messageSuggestion = models.TextField()

#for test
class Schedule(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=10)
    event_type = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    artist = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.date} - {self.event_type} by {self.artist}"