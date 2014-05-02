from meme import Meme
from result import Result
import re

class Parser():
    """Parses a list of Sources for instances of a meme"""

    def collate_words(self, meme, sources):
        regex = self._format_regex(meme)
        result = Result()
        for source in sources:
            match = re.search(regex, source.text, re.IGNORECASE)
            if match:
                result.add(match.groups()[0].lower(), source) #assumption: there was exactly one match
        return result 
    
    def _format_regex(self, meme):
        #assumes a valid meme
        return re.sub('\*', '([\\w\'\\-]+)', meme.get_body())
