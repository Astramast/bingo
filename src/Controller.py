class Controller:
	def __init__(self, view, model):
		self.view = view
		self.model = model
	
	def save(self):
		self.model.save()
	
	def checkBingo(self, case_number):
		self.model.checkBingo(case_number)
		self.view.swapColor(case_number)
		self.save()

