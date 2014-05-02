from meme import Meme
from result import Result
import re

class Parser():
    """Parses texts for instances of a meme"""

    def collate_words(self, meme, texts):
        regex = self._format_regex(meme)
        result = Result()
        for text in texts:
            match = re.search(regex, text, re.IGNORECASE)
            if match:
                result.add(match.groups()[0].lower()) #assumption: there was exactly one match
        return result 
    
    def _format_regex(self, meme):
        #assumes a valid meme
        return re.sub('\*', '([\\w\'\\-]+)', meme.get_body())
