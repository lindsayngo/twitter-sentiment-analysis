from django.shortcuts import render
from backend.main import twitter_api
import json
import pandas as pd

def analyze(request):
    return render(request, 'analyze.html')

def check(request):
    twt_api_connection = twitter_api.create_conn()
    hashtag = 'NFLX'
    count = '4'
    time_period = ''
    tweets = twt_api_connection.GetSearch(raw_query=f'q=%23{hashtag}&result_type=recent&count={count}')

    #parsed = json.loads(str(tweets[0]))
    #print(json.dumps(parsed, indent=4, sort_keys=True))

    parsedTweets = []
    for tweet in tweets:
        regSymbols = r'[\U00010000-\U0010ffff:/.#^,?@!-]'
        tweetText = tweet.text
        tweetText = tweetText.lower().replace(regSymbols, ' ')
        parsedTweets.append(tweetText)

    seriesTweets = pd.DataFrame({'tweet' : []})
    seriesTweets['tweet'] = parsedTweets

    print(seriesTweets)

    return render(request, 'analyze.html')