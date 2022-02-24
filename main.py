import sys
import os.path

from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlEngine, QQmlComponent
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty, QVariant, QUrl

from pyrogram import Client

api_id = 123
api_hash = "123"


class Bridge(QObject):
	def __init__(self):
		super().__init__()
		self.visibl = True

	cha = pyqtSignal()
	@pyqtProperty(bool, notify=cha)
	def visible(self):
		return self.visibl

	@pyqtProperty(bool, notify=cha)
	def notvisible(self):
		return not self.visibl

	@pyqtSlot()
	def toggleVisible(self):
		self.visibl = not self.visibl
		self.cha.emit()
		# button = self.root.findChild(QObject, "login1")
		# button.setProperty("visible", not button.getProperty("visible"))

#if __name__ == "__main__":

qapp = QApplication(sys.argv)
engine = QQmlApplicationEngine()

if os.path.isfile("account.session"):
	session = open("account.session").read()
	try:
		tgclient = Client(session)
	except:
		bridge.load


bridge = Bridge()
context = engine.rootContext()
context.setContextProperty("app", bridge)
engine.load('main.qml')


sys.exit(qapp.exec_())