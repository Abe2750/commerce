from pydoc import describe
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# def validate_bid()

from django.contrib.auth.models import User


class User(AbstractUser):
    pass

class Listing(models.Model):
    
    CATEGORY_CHOICES = [
        ('Toys', 'Toys'),
        ('Elec', 'Electronics'),
        ('Fash', 'Fashion'),
        ('Home', 'Home'),
       
    ]
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 200, primary_key= True)
    description = models.TextField()
    startBid = models.PositiveBigIntegerField()
    currentBidVal = models.PositiveBigIntegerField(default=0)
    image = models.URLField(null = True, blank = True)
    category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        default='Home',
        null = True
    )
    active = models.BooleanField(null = True, default=True)
    creator1 = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    winner = models.ForeignKey(User, on_delete = models.CASCADE, null = True,related_name= 'winner')

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name= "bids", primary_key= True)
    amount = models.IntegerField()
class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name= "bidz", primary_key=True)
    commentText = models.CharField(max_length=300)

class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watchList = models.ManyToManyField(Listing)