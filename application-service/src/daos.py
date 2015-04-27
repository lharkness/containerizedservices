import ZODB, ZODB.FileStorage, BTrees.OOBTree, transaction

from models import Application
from copy import deepcopy

class ApplicationDao:

	def __init__(self):
		storage = ZODB.FileStorage.FileStorage('/etc/application-service/data.db/mydata.fs')
		db = ZODB.DB(storage)
		connection = db.open()
		self.root = connection.root
		self.root.applications = BTrees.OOBTree.BTree()
	
	def save(self, application):
		self.root.applications[application.get_name()] = application
		transaction.commit()

	def retrieve(self, name):
		return self.root.applications[name]

	def delete(self, name):
		del self.root.applications[name]
		transaction.commit()

	def retrieve_all(self):
		return deepcopy(self.root.applications)
