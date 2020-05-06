from django.db import models

# Create your models here.

class Squad(models.Model):
    Country_Name = models.CharField(max_length=20)
    WorldCup_Group = models.CharField(max_length=1)
    Squad_Number = models.IntegerField()
    Position = models.CharField(max_length=3)
    Player_Name = models.CharField(max_length=30)
    Date_Of_Birth = models.DateField()
    Age = models.IntegerField()
    Caps = models.IntegerField()
    Goals = models.IntegerField()
    Club = models.CharField(max_length=30)

    def __str__(self):
        return self.Country_Name+ " - " + self.Player_Name
