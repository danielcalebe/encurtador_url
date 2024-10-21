from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = ''
    if request.method == 'POST':
        url = request.form['url']
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(url)
    return render_template('index.html', short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)
