from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from random import shuffle
from MainScreen import MainScreen
import os


class MyApp(App):
	def createBingo(self):
		bingo_list = [
			"Ils abandonnent", 
			"Ils dorment chez l'habitant", 
			"Ils se font poursuivre", 
			"Ils prennent le train en France", 
			"Ils se font aider par d'autres cyclistes"
		]
		
		solo_list = [
			"tombe",
			"déraille",
			"crève un pneu",
			"casse sa chaîne",
			"tombe malade",
			"pleure en premier",
			"se fait klaxonner",
			"descend en montée en premier",
			"perds un truc",
			"vomis"
		]
		
		for i in ["Baptiste ", "Nicolas "]:
			for j in solo_list:
				bingo_list.append(i + j)
		return bingo_list

	def build(self):
		self.ensureBingoFileExistence()
		sm = ScreenManager()
		sm.add_widget(MainScreen(name="main"))
		return sm

	def	ensureBingoFileExistence(self):
		print("Checking for bingo.txt")
		print(App.get_running_app().user_data_dir)
		if not os.path.exists(os.path.join(App.get_running_app().user_data_dir, "bingo.txt")):
			print("Creating bingo.txt")
			bingo_list = self.createBingo()
			shuffle(bingo_list)
			with open(os.path.join(App.get_running_app().user_data_dir, "bingo.txt"), "w") as f: 
				f.write(str(bingo_list))
			with open(os.path.join(App.get_running_app().user_data_dir, "check.txt"), "w") as f: 
				f.write(str([0] * len(bingo_list)))


if __name__ == "__main__":
	MyApp().run()

