from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MainScreen import MainScreen


class MyApp(App):
	def build(self):
		self.ensureDataExistence()
		self.sm = ScreenManager()
		self.sm.add_widget(MainScreen(name="main"))
		return self.sm
	
	def	ensureEventListExistence(self):
		with Database() as db:
			if not db.checkDataExistence():
				self.createData()
	
	def createEventList(self):
		with Database() as db:
			DEFAULT_EVENTLIST = db.getDefaultEventList()
		DEFINITIVE_EVENTLIST = DEFAULT_EVENTLIST.getRandomized()
		with Database() as db:
			db.writeDefinitiveEventList(DEFINITIVE_EVENTLIST)


if __name__ == "__main__":
	MyApp().run()

