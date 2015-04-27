from flask import Flask 
from flask import abort

from models import Application
from daos import ApplicationDao

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'

@app.route('/testbed/missing')
def error():
	flask.abort(400)

@app.route('/testbed/')
def hello_world():

	appDao = ApplicationDao()

	first_app = Application("first app")

	appDao.save(first_app)

	appDao.close()

	return repr(appDao.retrieve_all())

@app.route('/testbed/<name>', methods=['DELETE'])
def remove(name=None):
	if name is not None:
		app_dao = ApplicationDao()
		item = app_dao.retrieve(name)
		if item is not None:
			app_dao.delete(name)
			app_dao.close()
		else:
			return not_found() 
	else:
		return not_found()

	return "Deleted"

@app.route('/testbed/<name>', methods=['PUT', 'POST'])
def add(name=None):
	if name is not None:
		app_dao = ApplicationDao()
		app = Application(name)
		app_dao.save(app)
		app_dao.close()
		return "added"

	return not_found() 

@app.route('/testbed/<name>', methods=['GET'])
def retrieve(name=None):
	if name is not None:
		app_dao = ApplicationDao()
		app = app_dao.retrieve(name)
		if app is None:
			app_dao.close()
			return not_found()

		app_dao.close()
		return repr(app)
	else:
		return not_found() 

@app.route('/testbed/keys', methods=['GET'])
def get_keys():
	app_dao = ApplicationDao()
	keys = app_dao.get_keys()
	app_dao.close()
	return repr(keys)

@app.errorhandler(404)
def not_found(error=None):

	message = {
        	'status': 404,
  		'message': 'Not Found: ' + request.url,
    	}

	return repr(message)

if __name__ == '__main__':
    app.run('0.0.0.0', 5020)
