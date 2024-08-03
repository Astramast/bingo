from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from Database import Database
ACTIVE_COLOR = (0, 1, 0, 1) # GREEN
INACTIVE_COLOR = (1, 1, 1, 1) # WHITE


class MainScreen(Screen):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.grid = GridLayout(cols=5, rows=5, padding=10, spacing=10)
		with Database() as db:
			check = db.check
			bingo = db.bingo
		self.buttons = []
		for i in range(5):
			for j in range(5):
				case_number = i * 5 + j
				active = check[case_number]
				text = str(bingo[case_number])
				on_press = lambda b, x=i, y=j: self.check(x, y)
				background_color = ACTIVE_COLOR if active else INACTIVE_COLOR
				button = Button(text=text, on_press=on_press, background_color=background_color, halign="center", valign="middle", text_size=(None, None))
				button.bind(size=self._on_button_size)
				self.buttons.append(button)
		for button in self.buttons:
			self.grid.add_widget(button)
		self.add_widget(self.grid)
	
	def _on_button_size(self, button, size):
		button.text_size = (button.width, None)

	def check(self, i, j):
		case_number = i * 5 + j
		with Database() as db:
			db.checkBingo(case_number)
			self.buttons[case_number].background_color = ACTIVE_COLOR if db.check[case_number]==1 else INACTIVE_COLOR

