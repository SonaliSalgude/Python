class Mother:
	mothername = ""
	def mother(self):
        	print(self.mothername)

class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

class Son(Mother,Father):
	def parents(self):
		print("Mother name is:",self.mothername)
		print("Father name is:",self.fathername)

s1 = Son()
s1.mothername = "Sita"
s1.fathername = "Ram"
s1.parents()
	