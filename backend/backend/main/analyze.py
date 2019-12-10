import pandas as pd
from .models import *
from datetime import datetime
import os
from backend.main import twitter_api

def get_analysis_result(topic, conn):

    COUNT = '100' # free version of api limit
    tweets = conn.GetSearch(raw_query=f'q=%23{topic}&result_type=recent&count={COUNT}')

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

    # convert seriesTweets mean sentiment to integer because of djongo bug with decimals
    intRep = int(seriesTweets['polarity'].mean()*1000)

    # create new analysis of the requested hashtag
    htag = Hashtag.objects.get(topic=topic)
    return Analysis.objects.create(hashtag_id=htag,timeseries=[DataPoint(datetime.now(),intRep)])
    