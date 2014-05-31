"""Represents an individual source tweet"""

class Source():
    """Represents an individual source tweet"""

    def __init__(self, handle_id, handle_text, status_id, status_text):
        """Sources have a username, text and URL"""
        self.handle_id = handle_id
        self.handle_text = handle_text
        self.status_id = status_id
        self.status_text = status_text
