"""Flask Module and Classes import"""
from flask import Flask, render_template, request, jsonify
from .classes.parser import Parser
from .classes.google_api import GmApi
from .classes.wiki_api import WikiApi
from .config import GM_API_KEY

app = Flask(__name__)

@app.route('/')
def index():
    """Index page, with simply the form"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """Page to process POST request sent from Index Page's Form
    using AJAX with the form.js file to return every data
    """
    parser = Parser()
    question = request.form['question']
    #check if empty
    if not question:
        return jsonify({'error' : "Tu n'as rien demandé..."})
    string = parser.parse_sentence(question)
    #check if parsed string is empty
    if not string:
        return jsonify({'error' : "Je n'ai pas compris ta question."})

    api_gm, api_wiki = GmApi(GM_API_KEY), WikiApi()
    search = api_gm.request_search(string)
    #check if google map found something
    if not search:
        return jsonify({'error' : "J'ai compris la question," /
                        "mais je ne connais pas la réponse."})
    details = api_gm.request_details(search['place_id'])
    if not details:
        return jsonify({'error' : "Je connais cet endroit, mais " /
                        "je ne sais plus où c'est."})
    google_map = api_gm.request_map(details['address'], 15, "400x400")
    wiki_data = api_wiki.get_data(details['route'])
    story = parser.remove_titles(wiki_data['text'])

    return jsonify({'map' : google_map.url, 'story' : story,
                    'address' : details['address'], 'url' : wiki_data['url']})

        
    
