import os
from flask import Flask

app = Flask(__name__)
port = int(os.getenv('PORT', '3000'))
@app.route('/')
def home():
    return "<h1>Hello world, Running on SAP CloudFoundry</h1>"

@app.route('/test')
def test():
    return "<h2>Testing this endpoint, for CloudFoundry Automatic Push :)"
@app.route('/admin')
def admin_login():
    return "<h3>You are not authorized to perform login activity, Contact your Administrator for more help!!!</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
