"""Represents the results of parsing text for a meme"""

class Result():
    """Represents the results of parsing text for a meme"""

    def __init__(self):
        """Constructor"""
        self._words = {}
        self._sources = {}
        self.count = 0

    def add(self, word, source):
        """Records a word and its Source in the Result object"""
        #assumption: words are already lower case
        if word in self._words:
            self._words[word] += 1
        else:
            self._words[word] = 1

        #assumption: source is a Source object
        if word in self._sources:
            self._sources[word].append(source)
        else:
            self._sources[word] = [source]
        self.count += 1

    def get_list(self):
        """Returns a list of words, most frequently seen first"""
        return sorted([item for item in self._words.items()],
                      key=lambda x: x[1],
                      reverse=True)

    def get_source_list(self, word):
        """Returns a list of Sources for a word"""
        return self._sources[word]
