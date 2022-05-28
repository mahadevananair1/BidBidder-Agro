from django.shortcuts import render

# Create your views here.
from typing import Dict
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import AuctionForm, AuctionWatchers, Bidform, CommentForm
from .models import  Bid, Category, Comments, User,AuctionList
import operator

def index(request):
    try:
        obj_count = AuctionList.objects.filter(watchers = request.user).count()
    except:
        obj_count = ""   

    """ didint complete aution info view etc """
     # list of products available
    products = AuctionList.objects.filter(status = True)
    print(products)
    # checking if there are any products
    empty = False
    if len(products) == 0:
        empty = True
    
    return render(request, "auctions/index.html",{
        'watcher_count' : obj_count,
        'products':products,
        'empty': empty
    })