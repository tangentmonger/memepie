"""Represents an individual source tweet"""

class Source():
    """Represents an individual source tweet"""

    def __init__(self, handle, text, link):
        """Sources have a username, text and URL"""
        self.handle = handle
        self.text = text
        self.link = link
