from kivy.app import App
from os.path import join, exists
from random import shuffle
from FileManager import FileManager
from BingoParser import BingoParser


class Database:
	DATA_FILE = "bingo.txt"
	DEFAULT_FILE = "BINGO.txt"
	def __init__(self, directory):
		self.directory = directory
		self.file_manager = FileManager(directory)
		self.bingo_parser = BingoParser()
	
		if self.file_manager.checkFileExistence(self.DATA_FILE) == False:
			self.__buildBingo()
		self.check, self.bingo = self.__extractData()
	
	def __buildBingo(self):
		default_text = self.file_manager.getFileContent(self.DEFAULT_FILE)
		check, default_bingo = self.bingo_parser.parse(default_text)
		bingo = default_bingo[:]
		shuffle(bingo)
		self.__writeData(check, bingo)
	
	def __writeData(self, check, bingo):
		# Double \n because no names in the bingo file
		text = check + "\n\n" + "\n".join(bingo)
		self.file_manager.setFileContent(self.DATA_FILE, text)
	
	def __extractData(self):
		text = self.file_manager.getFileContent(self.DATA_FILE)
		check, bingo = self.bingo_parser.parse(text)
		return check, bingo
	
	def checkBingo(self, case_number):
		if self.check[case_number] == 1:
			self.check[case_number] = 0
		else:
			self.check[case_number] = 1
	
	def getBingo(self):
		return self.bingo[:]

