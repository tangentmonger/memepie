from meme import Meme
import re

class Parser():
    """Parses texts for instances of a meme"""

    def collate_words(self, meme, texts):
        regex = self._format_regex(meme)
        words = {}
        for text in texts:
            match = re.search(regex, text, re.IGNORECASE)
            if match:
                word = match.groups()[0].lower() #assumption: there was exactly one match
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
        return words            
    
    def _format_regex(self, meme):
        #assumes a valid meme
        return re.sub('\*', '([\\w\'\\-]+)', meme.get_body())
