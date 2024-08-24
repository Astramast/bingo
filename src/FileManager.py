from os.path import join, exists


class FileManager:
	def __init__(self, protected_files):
		self.protected_files = protected_files
	
	def getFileContent(self, file):
		with open(file, "r", encoding="utf-8") as f:
			text = f.read()
		return text
	
	def setFileContent(self, file, content):
		if file in self.protected_files:
			raise PermissionError("Cannot overwrite protected file.")
		with open(file, "w", encoding="utf-8") as f:
			f.write(content)
	
	def checkFileExistence(self, file):
		return exists(file)

