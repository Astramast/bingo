from kivy.app import App
from path import join


DEFAULT_FILE = "BINGO.txt"
DATAFILE = "bingo.txt"


class Database:
	def __init__(self, directory):
		self.filename = join(directory, DATAFILE)
		self.__buildBingo()
		self.check, self.bingo = self.__getData()

	def __getDefaultText(self):
		with open(DEFAULT_FILE, "r", encoding='utf-8') as f:
			text = f.read()
		return text
	
	def __splitFile(self, file_content):
		splitting_point = text.find("\n") + 1
		check = text[:splitting_point]
		bingo_text = text[splitting_point:]
		return check, bingo_text
	
	def __parseBingo(self, bingo_text):
		bingo_list = bingo.
	def __buildBingo(self):
		if self.filename EXISTS: # TODO
			return
		text = self.__getDefaultText()
		check, bingo_text = self.__splitFile(text)
		bingo = self.__parseBingo(bingo_text)

