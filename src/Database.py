from kivy.app import App
from os.path import join, exists
from random import shuffle
from FileManager import FileManager
from BingoParser import BingoParser


class Database:
	DEFAULT_FILE = "BINGO.txt"
	def __init__(self, directory):
		self.directory = directory
		self.file_manager = self.FileManager(directory)
		self.bingo_parser = self.BingoParser()
	
		if self.file_manager.checkDataExistence() == False:
			self.__buildBingo()
		self.check, self.bingo = self.__extractData()
	
	def __buildBingo(self):
		default_text = self.file_manager.getFileContent(join(self.directory, "BINGO.txt"))
		check, default_bingo = self.bingo_parser.parse(default_text)
		bingo = default_bingo[:]
		shuffle(bingo)
		print(bingo)
		self.file_manager.setDataContent(check + "\n" + "".join(bingo))

