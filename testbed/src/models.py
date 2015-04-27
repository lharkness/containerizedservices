import persistent

class ApplicationList(persistent.Persistent):
	def __init__(self):
		applications = []

	def add_application(app):
		applications.append(app)

	def remove_application(app):
		application.remove(app)

	def retrieve_all():
		return deepcopy(applications)

class Application(persistent.Persistent):
	
	def __init__(self, name):
		self.name = name
		self.ports = []
		self.ui_port = ""

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_ui_port(self):
		return self.ui_port

	def set_ui_port(self, ui_port):
		self.ui_port = ui_port

	def get_ports(self):
		return deepcopy(self.ports)

	def add_port(self, port):
		self.ports.append(port)

	def add_ports(self, ports):
		for port in ports:
			self.port.append(port)

	def to_string(self):
		print self.name
		print self.ui_port
		for port in self.ports:
			print port

