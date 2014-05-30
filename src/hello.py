from flask import Flask, render_template, request, g
import os
from meme import Meme
from twitter import Twitter
from src.parser import Parser #module name shadowing :(
from gchart import GChart


myapp = Flask(__name__)
myapp.debug = True

@myapp.route('/')
@myapp.route('/intro.htm')
def intro():
    return render_template("intro.htm") #looks in templates/
 
@myapp.route('/memepie.htm', methods=['GET'])
def memepie():
    if 'meme' in request.values:
        meme = Meme(request.values['meme'])
        if meme.is_valid():
            twitter = Twitter()
            parser = Parser()
            texts = twitter.get_sources(meme, 20)
            #from source import Source
            #texts = [Source("", "x is my middle name",""), Source("", "y is my middle name", ""), Source("", "x is my middle name","")]
            result = parser.collate_words(meme, texts)

            gchart = GChart()
            g.clean_query = meme.get_clean_meme()
            g.meme_exceptions = meme.get_exceptions()
            g.meme_parts = meme.get_parts()
            g.pie_data = gchart.generate_pie_data(result)

            #first_word_source_list = result.get_source_list(result.get_list()[0][0]) 
            return render_template("memepie.htm")
        else:
            return render_template("error.htm")

@myapp.route('/about.htm')
def about():
    return render_template("about.htm") #looks in templates/
 
