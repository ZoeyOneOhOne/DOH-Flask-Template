from flask import Flask
app = Flask(__name__)

@app.route('/<string:name>')
def hello_world(name):
    return f'Hello, {name}'

@app.route('/api', methods=['GET'])
def index():
    return {
        'name': 'Hello world!'
    }

if __name__ == '__main__':
    app.run(debug=True);