from django.shortcuts import render
from backend.main import twitter_api
import os
import json
import pandas as pd


def analyze(request):
    return render(request, 'analyze.html')

def check(request):
    twt_api_connection = twitter_api.create_conn()
    hashtag = 'mta'
    count = '100'
    time_period = ''
    tweets = twt_api_connection.GetSearch(raw_query=f'q=%23{hashtag}&result_type=recent&count={count}')

    lexicon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vader_lexicon.txt')
    lexiconDF = pd.read_csv(open(lexicon), sep='\t', header=None, names=('token', 'polarity', 'sentiment', 'list'))
    lexiconDF.drop(columns=['sentiment', 'list'], inplace=True)
    lexiconDF.set_index('token', inplace=True)

    parsedTweets = []
    #Cleaned every tweet
    for tweet in tweets:
        regSymbols = r'[\U00010000-\U0010ffff:/.#^,?@!-]'
        tweetText = tweet.text
        tweetText = tweetText.lower().replace(regSymbols, ' ')
        parsedTweets.append({'id': tweet.id, 'tweet': tweetText})

    seriesTweets = pd.DataFrame(parsedTweets)

    reformat = seriesTweets[['tweet']]
    reformat = reformat['tweet'].str.split(expand=True).stack().reset_index()
    reformat.columns = ['id', 'num', 'word']
    reformat.set_index('id', inplace=True)

    
    temp = pd.merge(reformat, lexiconDF, how='outer', left_on='word', right_index=True)
    temp = temp[pd.notnull(temp['num'])]
    temp = temp.groupby(temp.index).sum(level='polarity')
    temp = temp.drop(columns=['num', 'word'])
    seriesTweets = seriesTweets.merge(temp, left_index=True, right_index=True)


    print(seriesTweets)
    print(seriesTweets['polarity'].mean())

    return render(request, 'analyze.html')