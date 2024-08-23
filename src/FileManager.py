from os.path import join, exists


class FileManager:
	protected_files = ["BINGO.txt"]
	def __init__(self, directory):
		self.protected_files = [join(directory, protected_file) for protected_file in self.protected_files]
	
	def getFileContent(self, file):
		with open(file, "r", encoding="utf-8") as f:
			text = f.read()
		return text
	
	def setFileContent(self, file, content):
		if file == self.default_file:
			raise PermissionError("Cannot overwrite default file")
		with open(file, "w", encoding="utf-8") as f:
			f.write(content)
	
	def checkFileExistence(self, file):
		return exists(file)

