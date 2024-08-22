from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MainScreen import MainScreen
from Database import Database


class MyApp(App):
	def build(self):
		self.db = Database(App.get_running_app().user_data_dir)
		self.sm = ScreenManager()
		self.sm.add_widget(MainScreen(name="main"))
		return self.sm


if __name__ == "__main__":
	MyApp().run()

