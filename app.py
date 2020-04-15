from flask import Flask, jsonify, request, render_template, redirect, url_for
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

session = requests.session()
session.verify = False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        api_url = request.form.get('apiurl')
        if api_url:
            r = session.get(api_url + '/access-keys/')
            access_keys = r.json()['accessKeys']
            return render_template('access_keys.html', access_keys=access_keys)
        else:
            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
