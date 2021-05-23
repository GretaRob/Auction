from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ListingForm, CommentForm, BidForm

from .models import User, Listing, Comment, Bid


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, "auctions/index.html", context)


@login_required
def listing_form(request):
    form = ListingForm()
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = ListingForm(request.POST)
        if form.is_valid():
            # doesn't save right away in database
            listing = form.save(commit=False)
            listing.creator = user
            listing.save()
            return HttpResponseRedirect(reverse("index"))
    context = {'form': form}
    return render(request, 'auctions/listing_form.html', context)


@login_required
def comment_form(request, listing_id):
    user = User.objects.get(username=request.user)
    listing = Listing.objects.get(id=listing_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.save()
            listing.comments.add(comment)
            listing.save()
            return HttpResponseRedirect(reverse("index"))
    context = {'form': form,
               'listing_id': listing.id}
    return render(request, 'auctions/comment_form.html', context)


@login_required
def listing_page(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == "POST":
        user = User.objects.get(username=request.user)

        if not listing.closed:
            if request.POST.get("button") == "Close":
                listing.closed = True
                listing.save()
            else:
                price = request.POST["price"]
                bids = listing.bids.all()
                if user.username != listing.creator.username:  # only let those who dont own the listing be able to bid
                    if int(price) <= int(listing.price):
                        return render(request, "auctions/listing_page.html", {
                            "listing": listing,
                            "form": BidForm(),
                            "message": "Error! Invalid bid amount!"
                        })
                    form = BidForm(request.POST)
                    if form.is_valid():
                        # clean up this
                        bid = form.save(commit=False)
                        bid.user = user
                        bid.save()
                        listing.bids.add(bid)
                        listing.price = price
                        listing.save()
                    else:
                        return render(request, 'auctions/listing_page.html', {
                            "form": form
                        })
        return HttpResponseRedirect(reverse('listing_page', args=(listing.id,)))
    else:
        return render(request, "auctions/listing_page.html", {
            "listing": listing,
            "form": BidForm(),
            "message": ""
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
