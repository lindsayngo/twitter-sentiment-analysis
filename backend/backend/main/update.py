from twitter_api import get_tweets
from models import Subscription, Hashtag, Analysis
from views import check
import pandas as pd
from django.db.models import F

#decrease all frequencies
Subscription.objects.all().update(checked_since=F('checked_since') - 1)

twt_api_connection = twitter_api.create_conn()

time_period = '2019-12-05'
query_result = Subscription.objects.filter(checked_since=0).only("hashtag_id")
hashtag_ids = set(query_result)

for hashtag_id in hashtag_ids:
	hashtag_obj= Hashtag.objects.filter(pk=hashtag_id)
	tweets = twitter_api.get_tweets(hashtag_obj.topic, twt_api_connection)

	create_timeseries(hashtag_id, tweets)

# re-set checked since fields to frequency
for result in query_result:
	result.checked_since = result.frequency
bulk_update(results)


def create_timeseries(hashtag_id, tweets):
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
    new_analysis = Analysis.objects.create(hashtag_id=hashtag_id,timeseries=[DataPoint(datetime.datetime.now(),intRep)])
    print(new_analysis)