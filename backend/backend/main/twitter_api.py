import twitter
from .. import settings

TWEET_COUNT = 200

def create_conn():
	twt = settings.TWITTER_API_ACCESS
	api = twitter.Api(consumer_key = twt['TWT_API_KEY'],
	                  consumer_secret = twt['TWT_API_SECRET'],
	                  access_token_key = twt['TWT_ACCESS_TOKEN'],
	                  access_token_secret= twt['TWT_ACCESS_SECRET'],
	)
	return api

def get_tweets(hashtag, time_period):
  count = TWEET_COUNT
  api.GetSearch(raw_query=f'q=%23{hashtag}&result_type=recent&since={time_period}&count={count}')