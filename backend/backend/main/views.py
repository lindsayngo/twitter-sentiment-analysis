from django.shortcuts import render
from .models import *
from bson.objectid import ObjectId

import datetime

objects = models.DjongoManager()

# User request to subscribe to a hashtag - post
def subscribe(request):
    print(request.POST.get('username'))
    user = User.objects.get(username=request.POST.get('username'))
    print(user.username)
    topic = request.POST['topic']
    freq = request.POST['freq']

    # check if the hashtag is already in the database - if not, add it
    # get() raises a DoesNotExist exception if object is not found

    # *** not sure what the last scanned field should be for a newly created hashtag
    new_htag = Hashtag.objects.create(topic=topic, last_scanned=datetime.datetime.now())
    try:
        already_exists = Hashtag.objects.get(topic = topic)
    except:
        new_htag.save()
        new = new_htag

    # add a new subscription
    new_sub = Subscription.objects.create(user_id=user, hashtag_id=new_htag, frequency=freq)
    # new_sub.save()
    # return the user to their feed
    return render(request, 'feed.html')

# User request to delete subscriptions - post
def unsubscribe(request):
    user = User.objects.get(username=request.GET['username'])
    htag = Hashtag.objects.get(topic=request.POST.get('topic'))

    # remove subscription
    remove_sub = Subscription.objects.get(user_id = user, hashtag_id = htag)
    remove_sub.delete()

    return render(request, 'feed.html')

# User request to filter subscriptions
def filter(request):
    user = User.objects.get(username=request.GET['username'])
    filtered_subs = Subscription.objects.filter(user_id=request.POST.get('username'))

    return render(request, 'feed.html', {'user_subs': filtered_subs})

# Display User's subscribed hashtags - get
def feed(request):
    try:
        user = User.objects.get(username = request.POST.get('user'))
        user_subs = Subscription.objects.get( user_id = user )
        return render(request, 'feed.html', {'user_subs': user_subs})
    except:
        return render(request, 'feed.html')

# User registers
def register(request):
    new_user = User.objects.create(username=request.POST.get('username'), password=request.POST.get('password'))
    print(new_user)
    # new_user.save()
    return render(request, 'feed.html', {'user': request.POST.get('username')})

# User logs in
def login(request):
    # Authentication stuff ?
    try: 
        user = User.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
        return render(request, 'feed.html', {'user': user.username})
    except:
        return render(request, 'feed.html')


def home(request):

    return render(request, 'home.html')

