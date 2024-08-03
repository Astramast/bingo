from kivy.app import App
import os


class Database:
	def __init__(self):
		self.bingo_file = os.path.join(App.get_running_app().user_data_dir, "bingo.txt")
		self.check_file = os.path.join(App.get_running_app().user_data_dir, "check.txt")
		self.bingo = None
		self.check = None

	def load(self):
		with open(self.bingo_file, "r", encoding="utf-8") as f:
			self.bingo = eval(f.read())
		
		with open(self.check_file, "r", encoding="utf-8") as f:
			self.check = eval(f.read())
	
	def save(self):
		with open(self.check_file, "w", encoding="utf-8") as f:
			f.write(str(self.check))
	
	def checkBingo(self, i):
		self.check[i] = (self.check[i] + 1) % 2
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.save()
	
	def __enter__(self):
		self.load()
		return self

