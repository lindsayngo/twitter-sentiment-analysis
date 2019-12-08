from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from backend.main.analyze import get_analysis_result
import datetime
from django.db.models import Q

def home(request):
    return render(request, 'login.html')

# clear session, return to home
def logout(request):
    request.session.delete()
    return redirect("/login")

def login(request):
    if "user" in request.session:
        return redirect("/feed")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(Q(username=username), Q(password=password))
        if not user:
            return render(request, 'login.html', {'error': 'User does not exist'})
        request.session['user'] = username
        return redirect('/feed')
    return render(request, 'login.html')

def register(request):
    if "user" in request.session:
        return redirect("/feed")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(Q(username=username))
        if user:
            return render(request, 'register.html', {'error': 'Username is taken'})

        new_user = User.objects.create(username=username, password=password)
        request.session["user"] = username
        return redirect("/feed")
    return render(request, 'register.html')

def feed(request):
    if "user" not in request.session:
        return redirect("/login")

    uname = request.session.get("user")
    user = User.objects.get(username=uname)
    user_subs = Subscription.objects.filter(user_id = user)    

    error = request.session.get("subscription_error") or None
    graph = request.session.get("graph") or None

    # analysis_list = []
    # for s in user_subs:
    #     # for each subscription, retrieve the hashtag_id, find the analysis
    #     htagid = s.hashtag_id
    #     try:
    #         analysis = Analysis.objects.get(hashtag_id = htagid)
    #         analysis_list.append(analysis.timeseries[0].value)
    #     except:
    #         # analysis has not yet happened for the current hashtag
    #         analysis_list.append(-1)

    content = {'user': user.username, 'user_subs': user_subs, 'error': error, 'graph': graph}
    return render(request, 'feed.html', content)

def subscribe(request):
    if "user" not in request.session:
        return redirect("/login")

    uname = request.session.get("user")
    user = User.objects.get(username=uname)

    if request.method == 'POST':
        topic = request.POST['topic']
        freq = request.POST['freq']

        if freq.isdigit() and freq != "0":
            # create or get hashtag
            new_htag = Hashtag.objects.get_or_create(topic=topic)[0]
            
            # add new subscription
            Subscription.objects.create(user_id=user, hashtag_id=new_htag, frequency=int(freq))
            request.session['subscription_error'] = None

        else:
            error = "Frequency field must be a nonzero postive integer (X days)!"
            request.session['subscription_error'] = error

    return redirect('/feed')

def unsubscribe(request):
    if "user" not in request.session:
        return redirect("/login")

    if request.method == 'POST':
        uname = request.session.get("user")
        user = User.objects.get(username=uname)
        htag = request.POST.get('topic')

        htag = Subscription.objects.filter(user_id = user).filter(hashtag_id=htag)

        if htag:
            htag.delete()
            request.session['subscription_error'] = None
        else:
            error = "Subscription does not exist"
            request.session['subscription_error'] = error

    return redirect('/feed')

def analyze(request):
    if "user" not in request.session:
        return redirect("/login")

    uname = request.session.get("user")
    user = User.objects.get(username=uname)
    topic = request.GET.get('topic')
    htag = Subscription.objects.filter(user_id = user).filter(hashtag_id=topic)

    if htag:
        analysis = get_analysis_result(user, htag[0])
        print(analysis)

        # insert magic in templates to render graph
        request.session['graph'] = True 
        request.session['subscription_error'] = None
    else:
        error = "You are not subscribed to this hashtag"
        request.session['subscription_error'] = error

    return redirect('/feed')