import persistent

class Application(persistent.Persistent):
	
	def __init__(self):
		self.ports = []

	def __init__(self, name):
		self.ports = []
		self.name = name

	def __init__(self, name, ui_port):
		self.ports = []
		self.name = name
		self.ui_port = ui_port

	def get_name(self):
		return self.name


	def set_name(self, name):
		self.name = name

	
	def get_ui_port(self):
		return self.ui_port

	def set_ui_port(self, ui_port):
		self.ui_port = ui_port

	def add_port(self, port):
		self.ports.append(port)	

	def get_ports(self):
		return deepcopy(self.ports)
