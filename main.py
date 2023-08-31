import flask
import time
import json

app = flask.Flask(__name__)

API_URL = ""


def randomize_api_url():
    global API_URL
    API_URL = str(int(time.time()))


@app.route('/')
def index():
    randomize_api_url()
    return flask.render_template('index.html', api_url=API_URL)


@app.route('/api/<api_url>')
def api(api_url):
    OLD_API_URL = API_URL
    randomize_api_url()
    if api_url == OLD_API_URL:
        return json.dumps({'hello': 'world'})
    else:
        return "hello"


if __name__ == '__main__':
    app.run(debug=True)
