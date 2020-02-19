from flask import Flask, request, send_from_directory, render_template
app = Flask(__name__, static_url_path='', template_folder='C:\\Users\\Administrator\\Desktop\\python-docs-hello-world\\templates')

@app.route("/")
def index():
    return "Hello World!"

@app.route("/home")
def hello():
   return render_template('index.html')

@app.route('/img/<path:path>')
def send_js(path):
    return send_from_directory('img', path)