from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MainScreen import MainScreen
from Database import Database
from FileManager import FileManager
from BingoParser import BingoParser
from os.path import join


class MyApp(App):
	def build(self):
		DEFAULT_FILE = join(self.user_data_dir, "BINGO.txt")
		DATA_FILE = join(self.user_data_dir, "bingo.txt")
		PROTECTED_FILES = [DEFAULT_FILE]
		file_manager = FileManager(PROTECTED_FILES)
		bingo_parser = BingoParser()
		self.db = Database(DEFAULT_FILE, DATA_FILE, file_manager, bingo_parser)
		self.sm = ScreenManager()
		self.sm.add_widget(MainScreen(name="main"))
		return self.sm


if __name__ == "__main__":
	MyApp().run()

