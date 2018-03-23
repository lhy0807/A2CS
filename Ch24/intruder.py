class Status(object):

	def __init__(self):
		self.name = None
		self.buttons = []

	def getStatus(self):
		return self.name

	def changeStatus(self, newStatus):
		self.name = newStatus
		print("New status:", self.name, "\n")

class SystemActive(Status):

	def __init__(self):
		super().__init__()
		self.name = "SystemActive"
		self.buttons = [pressButton]

class AlertMode(Status):

	def __init__(self):
		super().__init__()
		self.name = "AlertMode"
		self.buttons = [pressButton, twoMinutesPass]

class AlarmBellRing(Status):

	def __init__(self):
		super().__init__()
		self.name

class AlarmSystem(object):

	def __init__(self):
		self.curStatus = Status("SystemInactive")

	def pressButton(self):
		if (self.curStatus.getStatus() == "SystemInactive"):
			self.curStatus.changeStatus("SystemActive")
		else: pass

	def sensorActivated(self):
		if (self.curStatus.getStatus() == "SystemActive"):
			self.curStatus.changeStatus("AlertMode")


	def enterPIN(self):
		if (self.curStatus.getStatus() == "SystemActive") \
			or (self.curStatus.getStatus() == "AlertMode") \
				or (self.curStatus.getStatus() == "AlarmBellRings"):

			self.curStatus.changeStatus("SystemInactive")

	def twoMinutesPass(self):
		if (self.curStatus.getStatus() == "AlertMode"):
			self.curStatus.changeStatus("AlarmBellRings")

	def showMenu(self):
		if (self.curStatus.getStatus() == "SystemInactive"):

