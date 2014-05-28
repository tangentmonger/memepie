import re
from meme import Meme
import urllib.parse
from TwitterSearch import *
from secrets import Secrets
from source import Source
import os
import datetime

class Twitter:
    """Interface to Twitter search API"""

    def get_sources(self, meme, number):
            
        #stdout available through Heroku logs
        print(" ".join([meme.get_body(), meme.get_exceptions()]))

        sources = []
        try:
            tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.setSearchURL(self._format_query(meme))
            tso.setLocale('en')
            tso.setCount(number) #smallest request that might work, but we'll probably need more
            tso.setIncludeEntities(False)

            ts = TwitterSearch(
                consumer_key = Secrets.consumer_key,
                consumer_secret = Secrets.consumer_secret,
                access_token = Secrets.access_token,
                access_token_secret = Secrets.access_token_secret
                )

            tweets = ts.searchTweets(tso)
            
            retries = 0;
            while len(sources) < number and retries < 5:
                for tweet in tweets['content']['statuses']:
                    sources.append(Source(tweet['user']['name'], tweet['text'], tweet['id_str']))
                    #print(tweet['text']) #there's a lot of strange characters coming in here
                tweets = ts.searchNextResults()
                retries += 1

        except TwitterSearchException as e:
            print(e, file=log, end='\n')

        return sources

    def _format_query(self, meme):
        #assumption: the meme is valid
        formatted_query = '"%s" %s' % (meme.get_body(), meme.get_exceptions())
        parameters = urllib.parse.urlencode({"q":formatted_query})
        return "?%s" % parameters


