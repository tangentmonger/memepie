from flask import Flask, render_template, request, g
import os
from meme import Meme
from twitter import Twitter
from parser import Parser
from gchart import GChart

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/intro.htm')
def intro():
    return render_template("intro.htm") #looks in templates/
 
@app.route('/memepie.htm', methods=['GET'])
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


#if __name__ == '__main__':
#    port = int(os.environ.get('PORT', 5000))
#    app.run(host='0.0.0.0', port=port)
