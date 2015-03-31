from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	return "Index"

@app.route('/application_service/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run('0.0.0.0', 5010)
