from twitter_api import get_tweets
from models import Subscription, Hashtag, Analysis
#from settings import time_period

time_period = '2019-12-05'
query_result = Subscription.objects.filter(upd_freq=0).only("hashtag_id")
query_result = set(query_result)

for hashtag_id in query_result:
	hashtag_obj= Hashtag.objects.filter(pk=hashtag_id)
	hashtag_update = twitter_api.get_tweets(hashtag_obj.topic, time_period)

	# Make call to the analysis API; results=
	analysis = Analysis(hashtag_id=hashtag_id, timeseries=results)
	analysis.save()

'''
profile_ids = []
	for result in result_list:
		profile_ids.append(sub.get('user_id'))
	profiles = User.objects.filter(pk__in=profile_ids)
	profiles = list(profiles)
'''