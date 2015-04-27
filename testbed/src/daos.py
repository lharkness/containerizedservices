import ZODB, ZODB.FileStorage, BTrees.OOBTree, transaction

from models import Application
from copy import deepcopy

class ApplicationDao:

	def __init__(self):
		self.storage = ZODB.FileStorage.FileStorage('/etc/testbed/data.db/mydata.fs')
		db = ZODB.DB(self.storage)
		self.connection = db.open()	
		self.db = self.connection.root()
	
	def save(self, application):
		self.db[application.get_name().encode("utf-8")] = application
		transaction.commit()

	def retrieve(self, name):
		try:
			item = self.db[name.encode("utf-8")]
		except KeyError:
			return None
		return item 

	def delete(self, name):
		try:
			del self.db[namei.encode("utf-8")]
			transaction.commit()
		except KeyError:
			pass

	def retrieve_all(self):
		items = []
		for key in self.db.keys():
			item = self.db[key]
			if isinstance(item, Application):
				items.append(item)
		
		return items 

	def get_keys(self):
		items = []
		for key in self.db.keys():
			items.append(key)
	
		return items

	def close(self):
		transaction.get().abort()
		self.connection.close()
		self.storage.close()
