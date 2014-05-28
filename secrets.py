import os

class Secrets():
    """API keys for accessing Twitter. Insert your own here."""

    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    access_token = os.environ['access_token']
    access_token_secret = os.environ['access_token_secret']
