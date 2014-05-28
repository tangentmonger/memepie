"""Handles Twitter search details"""

import urllib.parse
import TwitterSearch
from secrets import Secrets
from source import Source

class Twitter:
    """Interface to Twitter search API"""

    def get_sources(self, meme, number):
        """Fetches a list of Sources from Twitter that match the given meme"""
        #stdout available through Heroku logs. TODO: syslog
        print(" ".join([meme.get_body(), meme.get_exceptions()]))

        sources = []
        try:
            tso = TwitterSearch.TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.setSearchURL(self._format_query(meme))
            tso.setLocale('en')
            tso.setCount(number) #smallest request that might work
            tso.setIncludeEntities(False)

            twitter_search = TwitterSearch.TwitterSearch(
                consumer_key = Secrets.consumer_key,
                consumer_secret = Secrets.consumer_secret,
                access_token = Secrets.access_token,
                access_token_secret = Secrets.access_token_secret
                )

            tweets = twitter_search.searchTweets(tso)
            retries = 0
            while len(sources) < number and retries < 5:
                for tweet in tweets['content']['statuses']:
                    sources.append(Source(  tweet['user']['name'],
                                            tweet['text'],
                                            tweet['id_str']))
                    #print(tweet['text'])
                    #there's a lot of strange characters coming in here
                tweets = twitter_search.searchNextResults()
                retries += 1

        except TwitterSearch.TwitterSearchException as exception:
            print(exception) #TODO: syslog

        return sources

    @classmethod
    def _format_query(cls, meme):
        """Creates a query string from a Meme"""
        #assumption: the meme is valid
        formatted_query = '"%s" %s' % (meme.get_body(), meme.get_exceptions())
        parameters = urllib.parse.urlencode({"q":formatted_query})
        return "?%s" % parameters


