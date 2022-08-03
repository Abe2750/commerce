from dataclasses import fields
from django.forms import ModelForm
from auctions.models import Listing,Bid,Comment

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'startBid', 'image', 'category']
        #fields = "__all__"

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['commentText']