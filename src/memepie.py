"""Used to examine output of meme analysis system without GUI frontend"""

from meme import Meme
from twitter import Twitter
from parser import Parser

#m = Meme("all your * are belong to us -base")
#m = Meme("the internet is a * place")
#m = Meme("* is the new black")
meme = Meme("Milano è *")
twitter = Twitter()
parser = Parser()

texts = twitter.get_sources(meme, 100)
print([text.text for text in texts])
result = parser.collate_words(meme, texts)
print(result.get_list())
print(result.count)
first_word_source_list = result.get_source_list(result.get_list()[0][0])
print([source.link for source in first_word_source_list])

