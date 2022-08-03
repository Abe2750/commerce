from pydoc import describe
import re
from turtle import title
from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Bid, User,Listing, Visitor,Comment
from .forms import ListingForm , BidForm,CommentForm


def index(request):
    return render(request, "auctions/index.html", {
        "listings" : Listing.objects.all(), 
        "wins" : getWin(request),
        'watchList' : False,

    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def createlisting(request):
    if request.method == "POST":
        ListingForm2 = ListingForm(request.POST)
        if ListingForm2.is_valid():
            title1 = request.POST["title"]
            description1 = request.POST["description"]
            startBid1 = request.POST["startBid"]
            image1 = request.POST["image"]
            category1 = request.POST["category"]

           


        
        # Attempt to create new Listing
        try:
            listing = Listing(title = title1, description = description1, startBid = startBid1
            , image = image1, category = category1,active = True,creator1 = request.user)
            listing.save()
        except IntegrityError:
            return render(request, "auctions/createlisting.html", {
                "message": "Lising already exists."
            })
        return HttpResponseRedirect(reverse("index"))
    else:
        ListingForm1 = ListingForm()

        return render(request, 'auctions/createlisting.html', {'Listingform': ListingForm1})

def listingPage(request, listing):
     
    if request.method == "POST":
        if 'Place Bid' in request.POST:
            
            listing1 = Listing.objects.get(title = listing)
            BidForm2 = ListingForm(request.POST)
            amount1 = request.POST["amount"]
            if BidForm2.is_valid():
                amount1 = request.POST["amount"]
                
                        
            
            try:
                if validated(amount1,listing1):
                    bid = Bid(listing = listing1,amount = amount1,bidder = request.user)
                    listing1.currentBidVal = amount1
                    listing1.save()
                    bid.save()
                else :
                    return render(request, "auctions/Listing.html", {
                    'ListingUsed' : listing1,
                    'BidForm' : BidForm, 
                    'add' : request.user.visitor.watchList.filter(title = listing).exists(),
                    'message' : True,
                    'creator' : request.user == listing1.creator1,
                    'won' : False,
                    'CommentForm' : CommentForm,
                    'comments' : Comment.objects.all().filter(listing = listing1)
                    })               
            except IntegrityError:
                return HttpResponseRedirect(reverse("index"))
            return HttpResponseRedirect(reverse("index"))
        elif 'Add to Watchlist' in request.POST:
            addOrRemovewatch(request,listing)
        elif 'Remove from Watchlist' in request.POST:
            addOrRemovewatch(request,listing)
        elif 'Close Bid' in request.POST:
            closeBid(request,listing)
        elif 'Comment' in request.POST:
            comment(request,listing)
    else:
        print("here friend")
        BidForm1 = BidForm()
        try:
            add1 = request.user.visitor.watchList.filter(title = listing).exists()
        except AttributeError:
            add1 = False
        listing1 = Listing.objects.get(title = listing)
        return render(request, "auctions/Listing.html", {
            'ListingUsed' : listing1,
            'BidForm' : BidForm, 
            'add' : add1,
            'message' : False,
            'creator' : request.user == listing1.creator1,
            'won':False,
            'CommentForm' : CommentForm,
            'comments' : Comment.objects.all().filter(listing = listing1)
        })
    
    listing1 = Listing.objects.get(title = listing)
    return render(request, "auctions/Listing.html", {
            'ListingUsed' : listing1,
            'BidForm' : BidForm,
            'add' : request.user.visitor.watchList.filter(title = listing).exists(),
            'message' : False,
            'creator' : request.user == listing1.creator1,
            'won' :False,
            'CommentForm' :CommentForm,
            'comments' : Comment.objects.all().filter(listing = listing1)

        })
   
        

def addOrRemovewatch(request,listing):
    listing1 = Listing.objects.get(title = listing)
    

    if request.user.visitor.watchList.filter(title = listing).exists():
       
        request.user.visitor.watchList.remove(listing)
    else: 
        request.user.visitor.watchList.add(listing1)
    return HttpResponseRedirect(reverse("index"))

def validated(amount,listing):
    return int(amount) > listing.currentBidVal and int(amount) > listing.startBid
def closeBid(request,listing):
    listing1 = Listing.objects.get(title = listing)
    listing1.winner = Bid.objects.get(amount = listing1.currentBidVal).bidder
    listing1.active = False
    listing1.save()
def getWin(request):
     listings = Listing.objects.all()
     wins = []
     for listing in listings :
        if listing.winner == request.user:
            wins.append(listing)
     return wins 
def listingPage2(request, listing):
    BidForm1 = BidForm()
    listing1 = Listing.objects.get(title = listing)
    return render(request, "auctions/Listing.html", {
            'ListingUsed' : listing1,
            'BidForm' : BidForm,
            'add' : request.user.visitor.watchList.filter(title = listing).exists(),
            'message' : False,
            'creator' : request.user == listing1.creator1,
            'won' : True,
            'CommentForm' : CommentForm,
            'comments' : Comment.objects.all().filter(listing = listing1)

        })
def comment(request,listing):
    
    listing1 = Listing.objects.get(title = listing)
    print(Comment.objects.all().filter(listing = listing1))
    commentText1 = request.POST['commentText']
    print(request.POST['commentText'])
    comment1 = Comment(commentText = commentText1, listing = listing1 ,commenter = request.user)
    comment1.save()
def watchList(request):
    print(request.user.visitor.watchList)
    return render(request, "auctions/index.html", {
        "listings" : request.user.visitor.watchList.all(), 
        "wins" : getWin(request),
        'watchList' : True
    })
def categories(request):
    return render(request, "auctions/categories.html",{
            'Toys' : "Toys",
            "Home" : "Home",
            "Electronics" : "Elec",
            "Fashion" : "Fash"
        })
def categories2(request,name):
    print(Listing.objects.all().filter (category = name))
    return render(request, "auctions/index.html", {
        "listings" : Listing.objects.all().filter(category = name), 
        "wins" : getWin(request),
        'watchList' : False
    })
    