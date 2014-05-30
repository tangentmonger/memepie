"""Parses a list of Sources for instances of a meme"""

from result import Result
import re

class Parser(object):
    """Parses a list of Sources for instances of a meme"""

    def __init__(self):
        pass

    def collate_words(self, meme, sources):
        """Given a list of Sources and a Meme, populate a Result
        object with matching words"""
        regex = self._format_regex(meme)
        result = Result()
        for source in sources:
            match = re.search(regex, source.text, re.IGNORECASE)
            if match:
                result.add(match.groups()[0].lower(), source)
                #assumption: there was exactly one match
        return result

    def _format_regex(self, meme):
        """Generate a regex from a Meme"""
        #assumes a valid meme
        return re.sub('\*', '([\\w\'\\-]+)', meme.get_body())
