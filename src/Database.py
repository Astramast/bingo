from kivy.app import App
from path import join


class Database:
	class FileLoader:
		DEFAULT_FILE = "BINGO.txt"
		DATAFILE = "bingo.txt"
		def __init__(self, directory):
			self.filename = join(directory, DATAFILE)
		
		def getFileContent(self):
			with open(filename, "r", encoding='utf-8') as f:
				text = f.read()
			return text
		
		def setFileContent(self, content):
			with open(filename, "w", encoding='utf-8') as f:
				f.write(content)
	
	class BingoParser:
		def __buildBingoList(self, bingo_text):
			total_list = bingo_text.split("\n")
			names = total_list.pop(0).split(",")
			XX_list = []
			bingo_list = []
			for elem in total_list:
				if "XX" in elem:
					XX_list.append(elem)
				else:
					bingo_list.append(elem)
			for name in names:
				for i in XX_list:
					bingo_list.append(i.replace("XX", name))
			return bingo_list
		
		def __splitFile(self, file_content):
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
		self.file_loader = self.FileLoader(directory)
		self.bingo_parser = self.BingoParser()
	
		self.__buildBingo()
		self.check, self.bingo = self.__getData()
	
	def __buildBingo(self):
		if path.exists(DATAFILE):
			return
		text = self.file_loader.getFileContent()
		bingo = self.bingo_parser.parse(text)
		self.__setData(bingo)

