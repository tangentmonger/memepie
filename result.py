class Result():
    """Represents the results of parsing text for a meme"""

    def __init__(self):
        self._words = {}
        self.count = 0

    def add(self, word):
        #assumption: words are already lower case
        if word in self._words:
            self._words[word] += 1
        else:
            self._words[word] = 1
        self.count += 1

    def get_list(self):
        return sorted([item for item in self._words.items()], key=lambda x:x[1], reverse=True)
