class Controller:
	def __init__(self, view_factory, model_factory):
		self.view = view_factory.generateView(self)
		self.model = model_factory.generateView(self)
	
	def onCaseClick(self, case_number):
		self.model.changeCaseState(case_number)
	
	def onCaseDataChanged(self, case_number, state):
		self.view.changeCaseState(case_number, state)

