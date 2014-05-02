class Result():
    """Represents the results of parsing text for a meme"""

    def __init__(self):
        self._words = {}
        self._sources = {}
        self.count = 0

    def add(self, word, source):
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
        return sorted([item for item in self._words.items()], key=lambda x:x[1], reverse=True)

    def get_source_list(self, word):
       return self._sources[word] 
