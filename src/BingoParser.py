class BingoParser:
	def parse(self, content):
		check, names, raw_bingo = self.__splitContent(content)
		bingo = self.__buildBingo(raw_bingo, names)
		return check, bingo
	
	def __splitContent(self, content):
		content_list = content.split("\n")
		check = content_list.pop(0)
		names = content_list.pop(0).split(",")
		return check, names, content_list
	
	def __buildBingo(self, raw_bingo, names):
		bingo = []
		if raw_bingo[-1] == "":
			raw_bingo.pop(-1)
		for elem in raw_bingo:
			if "XX" in elem:
				for name in names:
					bingo.append(elem.replace("XX", name))
			else:
				bingo.append(elem)
		return bingo

