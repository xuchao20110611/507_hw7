from flask import Flask,render_template
import requests
from hw7secrets import api_key
app = Flask('hw7')

@app.route('/')
def index():
    return render_template('hw7_index.html')

@app.route('/name/<name>')
def name(name):
    return render_template('name.html',name=name)

@app.route('/headlines/<name>')
def headlines(name):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    results = requests.get(base_url, params).json()['results']
    fiveTitles=[]
    for i in range(5):
        fiveTitles.append((results[i]['title'],results[i]['url']))
    return render_template('headlines.html', name=name,title_list=fiveTitles)


@app.route('/links/<name>')
def links(name):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    results = requests.get(base_url, params).json()['results']
    fiveTitles=[]
    for i in range(5):
        fiveTitles.append((results[i]['title'],results[i]['url']))
    return render_template('links.html', name=name,title_list=fiveTitles)

@app.route('/images/<name>')
def images(name):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    results = requests.get(base_url, params).json()['results']
    fiveTitles=[]
    for i in range(5):
        fiveTitles.append((results[i]['title'],results[i]['url'],results[i]['multimedia'][0]['url']))
    return render_template('images.html', name=name,title_list=fiveTitles)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
