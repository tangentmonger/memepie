import re

class Meme:
    """Represents a meme typed in by the user, offering parsed versions of it"""
  
    def __init__(self, meme):
        self.raw_meme = meme

    def get_body(self):
        #remove exceptions, keep the remaining valid characters
        return re.sub("\\s+\\-[\\w']+", "", self.get_clean_meme())
       
    def get_exceptions(self):
        return "".join(re.findall("\\s+\\-[\\w']+", self.get_clean_meme())).strip()

    def is_valid(self):
        #considered valid if we have something sensible left after parsing
        return re.match('^[^*]*\*[^*]*$', self.get_body()) is not None
    
    def get_clean_meme(self):
        #remove anything weirdlooking from the query. 
        #allowed: alphanumeric, space, hyphen, asterisk, plus, apostrophe
        #not allowed: comma, period (Twitter search treats these as separators)
        temp = re.sub("[^A-Za-z0-9 *+'-]+", "", self.raw_meme)
        temp = re.sub(' +', ' ', temp.strip())
        return temp

    def get_parts(self):
        #return a list of the parts of the meme
        return [x.strip() for x in self.get_body().split("*")]
