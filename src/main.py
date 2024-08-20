from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from random import shuffle
from MainScreen import MainScreen
import os


class MyApp(App):
	def build(self):
		self.ensureDataExistence()
		self.sm = ScreenManager()
		self.sm.add_widget(MainScreen(name="main"))
		return self.sm

	def	ensureDataExistence(self):
		with Database() as db:
			if not db.checkDataExistence():
				self.createData()

	def createData(self):
		with Database() as db:
			default_bingo = db.getDefaultBingo()


if __name__ == "__main__":
	MyApp().run()

