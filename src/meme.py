"""Represents a meme typed in by the user, offering parsed versions of it"""
import re

class Meme:
    """Represents a meme typed in by the user, offering parsed versions of it"""

    def __init__(self, meme):
        """Initialise with the meme as typed by the user"""
        self.raw_meme = meme

    def get_body(self):
        """Extract the body of the meme"""
        #remove exceptions, keep the remaining valid characters
        #accents are valid characters!
        return re.sub("\\s+\\-[\\w']+", "", self.get_clean_meme())

    def get_exceptions(self):
        """Extract the exceptions of the meme, if any"""
        exceptions = re.findall("\\s+\\-[\\w']+", self.get_clean_meme())
        return "".join(exceptions).strip()

    def is_valid(self):
        """Meme considered valid if we have
        something sensible left after parsing"""
        return re.match(r'^[^*]*\*[^*]*$', self.get_body()) is not None

    def get_problem(self):
        """Try to diagnose problem with an invalid meme"""
        extracted_meme = self.get_clean_meme()
        error = "looks fine"
        if '*' not in extracted_meme:
            error = "has no wildcard (*)"
        elif extracted_meme.count('*') > 1:
            error = "has too many wildcards (*)"
        return error

    def get_clean_meme(self):
        """Remove anything weirdlooking from the query.
        Allowed: alphanumeric, space, hyphen, asterisk, plus, apostrophe, accents
        Not allowed: comma, period (Twitter search treats these as separators)
        """
        temp = re.sub("[^\\w *+'-]+", "", self.raw_meme)
        temp = re.sub(' +', ' ', temp.strip())
        return temp

    def get_parts(self):
        """Return a list of the parts of the meme"""
        return [x.strip() for x in self.get_body().split("*")]
