
class Student(object):
	def get_spec_name(self):
		self.__name = "special"
		print self.__name
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def printscore(self):
		print "%s\'s score: %d" %(self.name, self.score)
	def modscore(self, score):
		if 0 <= score <= 100:
			self.score = score
		else:
			raise ValueError("bad score")



		