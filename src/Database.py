from kivy.app import App
from random import shuffle
from os.path import join, exists


class Database:
	class FileManager:
		DEFAULT_FILE = "BINGO.txt"
		DATAFILE = "bingo.txt"
		def __init__(self, directory):
			self.default_file = join(directory, self.DEFAULT_FILE)
			self.data_file = join(directory, self.DATAFILE)
		
		def __getFileContent(self, file):
			with open(file, "r", encoding='utf-8') as f:
				text = f.read()
			return text
		
		def getDefaultContent(self):
			return self.__getFileContent(self.default_file)
		
		def getDataContent(self):
			return self.__getFileContent(self.data_file)
		
		def setDataContent(self, content):
			with open(self.data_file, "w", encoding='utf-8') as f:
				f.write(content)
		
		def checkDataExistence(self):
			return exists(self.data_file)
	
	class BingoParser:
		def __buildBingoList(self, bingo_text):
			total_list = bingo_text.split("\n")
			names = total_list.pop(0).split(",")
			bingo_list = []
			for elem in total_list:
				if "XX" in elem:
					for name in names:
						bingo_list.append(elem.replace("XX", name))
				else:
					bingo_list.append(elem)
			return bingo_list
		
		def __splitFile(self, text):
			splitting_point = text.find("\n") + 1
			check = text[:splitting_point]
			bingo_text = text[splitting_point:]
			return check, bingo_text
		
		def parse(self, text):
			check, bingo_text = self.__splitFile(text)
			bingo = self.__buildBingoList(bingo_text)
			return check, bingo
	
	def __init__(self, directory):
		self.directory = directory
		self.file_manager = self.FileManager(directory)
		self.bingo_parser = self.BingoParser()
	
		self.__buildBingo()
	
	def __buildBingo(self):
		if self.file_manager.checkDataExistence():
			return
		default_text = self.file_manager.getDefaultContent()
		check, default_bingo = self.bingo_parser.parse(default_text)
		bingo = default_bingo[:]
		shuffle(bingo)
		print(bingo)
		self.file_manager.setDataContent(check + "\n" + "".join(bingo))

