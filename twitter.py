import re
from meme import Meme
import urllib.parse
from TwitterSearch import *
from secrets import Secrets
import os

class Twitter:
    """Interface to Twitter search API"""

    #resource_url = "https://api.twitter.com/1.1/search/tweets.json?"
    queries_logfile = "queries.log"
    errors_logfile = "errors.log"

    def get_texts(self, meme, number):
        with open(self.queries_logfile, 'a') as log:
            print(" ".join([meme.get_body(), meme.get_exceptions()]), file=log, end='\n')

        texts = []
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
            while len(texts) < number and retries < 5:
                for tweet in tweets['content']['statuses']:
                    texts.append(tweet['text'])
                    #print(tweet['text']) #there's a lot of strange characters coming in here
                tweets = ts.searchNextResults()
                retries += 1

        except TwitterSearchException as e:
            with open(self.errors_logfile, 'a') as log:
                print(" ".join([meme.get_body(), meme.get_exceptions()]), file=log, end='\n')
                print(e, file=log, end='\n')

        return texts

    def _format_query(self, meme):
        #assumption: the meme is valid
        formatted_query = '"%s" %s' % (meme.get_body(), meme.get_exceptions())
        parameters = urllib.parse.urlencode({"q":formatted_query})
        return "?%s" % parameters


