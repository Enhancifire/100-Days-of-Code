from flask import Flask, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))

if __name__ == "__main__":
    app.run(debug=True)
