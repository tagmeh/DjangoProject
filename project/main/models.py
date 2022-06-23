from django.db import models

# Create your models here.


class ColorOptions(models.TextChoices):
    BLUE = "Blue"
    TEAL = "Teal"
    CYAN = "Cyan"
    YELLOW = "Yellow"
    GREEN = "Green"
    RED = "Red"
    PURPLE = "Purple"
    CHARTREUSE = "Chartreuse"
    SALMON = "Salmon"
    ORANGE = "Orange"
    WHITE = "White"
    BLACK = "Black"
    BROWN = "Brown"
    GREY = "Grey"


class PlayerTypes(models.TextChoices):
    KING = "King"
    KNIGHT = "Knight"
    SQUIRE = "Squire"
    PATSY = "Patsy"
    FRENCHMAN = "Frenchman"
    ENCHANTER = "Enchanter"
    COMMONER = 'Commoner'


class Companion(models.Model):
    name = models.CharField(max_length=100)
    favorite_color = models.CharField(choices=ColorOptions.choices, max_length=50)
    number_coconuts = models.IntegerField()


class Player(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(choices=PlayerTypes.choices, max_length=50, default=PlayerTypes.COMMONER)
    favorite_color = models.CharField(choices=ColorOptions.choices, max_length=50)
    age = models.IntegerField()
    quest = models.CharField(max_length=200, null=True, blank=True)
    assigned_companion = models.ForeignKey(Companion, on_delete=models.CASCADE, null=True, blank=True)
    quest_complete = models.BooleanField(default=False)


