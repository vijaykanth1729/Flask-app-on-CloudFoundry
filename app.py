import os
from flask import Flask

app = Flask(__name__)
port = int(os.getenv('PORT', '3000'))
@app.route('/')
def home():
    return "<h1>Hello world, deployed successfully with updation</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

