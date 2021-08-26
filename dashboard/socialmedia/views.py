from django.shortcuts import render
from pymongo import MongoClient

client = MongoClient('3.134.245.186', 27017)

db = client.sponsorlytix

# Create your views here.
def facebook(request):
    posts = list(db.social_media_posts.find())
    print(posts)
    data = { 'd': posts}
    return render(request, 'index.html', data)

def twitter(request):
    posts = list(db.twitter_metrics.find())
    print(posts[0])
    data = { 'd': posts}
    return render(request, 'twitter.html', data)

def instagram(request):
    posts = list(db.instagram_metrics.find())
    print(posts[0])
    data = { 'd': posts}
    return render(request, 'instagram.html', data)

