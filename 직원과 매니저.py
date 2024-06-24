class Employee:
	#name,base,extra
	def __init__(self,name,base,extra=0):
		self.name=name
		self.base=base
		self.extra=extra
	
	def calc_salary(self):
		return self.base+self.extra
	
	def plus_extra(self,num):
		self.extra+=num
	
	def __str__(self):
		print("이름:",self.name)
		print("기본금:",self.base)
		print("초과근무액:",self.extra)
		print("총 월급:",self.calc_salary())
	
	
class Manager(Employee):
	#add
	def __init__(self,name,base,extra,add):
		super().__init__(name,base,extra)
		self.add=add
	
	def cal_salary(self):
		return self.base+self.extra+self.add
	
	def __str__(self):
		print("이름:",self.name)
		print("기본금:",self.base)
		print("초과근무액:",self.extra)
		print("추가수당",self.add)
		print("총 월급:",self.cal_salary())
	

emp1=Employee("홍길동",200)
emp2=Employee("이영희",220)
man=Manager("김철수",250,0,30)
emp1.__str__()
print("===================")

emp2.__str__()
print("===================")

man.__str__()
print("===================")


emp1.plus_extra(60)
emp1.plus_extra(50)
emp1.__str__()
print("===================")

emp2.plus_extra(60)
emp2.plus_extra(60)
emp2.plus_extra(60)
emp2.__str__()
print("===================")

man.plus_extra(50)
man.plus_extra(50)
man.__str__()
print("===================")