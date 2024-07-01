import re
class Stack:
	def __init__(self):
		self.top=[]
	
	def isEmpty(self):
		return len(self.top)==0
	
	def size(self):
		return len(self.top)
	
	def push(self,item):
		self.top.append(item)
		
	def pop(self):
		if not self.isEmpty():
			return self.top.pop(-1)
		
	def peek(self):
		if not self.isEmpty():
			return self.top[-1]
	
	def clear(self):
		self.top=[]
		
		
def checkkai(inputted):
	stack=Stack()
	inputted = re.sub(r'[^a-zA-Z0-9]', '', inputted)
	for gul in inputted:
		if gul.isalnum:
			stack.push(gul)
	for i in range(int(stack.size()/2)):
		now=stack.pop()
		if inputted[i] != now:
			return False
	return True
	
	
inputted=input("회문 체크용 문자열:")
if(checkkai(inputted)):
	print(inputted,"회문임")
else:
	print(inputted,"회문이 아님")
		
		
		
		
"""		
def isValidPos(x,y):
	if x<0 or y<0 or x>=MAX_SIZE or y>=MAX_SIZE:
		return False
	else:
		return map[x][y]=='0' or map[x][y]=='x'
	
	
def DFS():
	stack=Stack()
	stack.push((1,0))
	print('DFS:')
	
	while not stack.isEmpty():
		here=stack.pop()
		print(here,end='->')
		(x,y)=here
		if map[x][y]=='x':
			return True
		else:
			map[x][y] = '.'  # 현재위치를 지나왔다고 '.' 표시
			if isValidPos(x - 1, y):
				stack.push((x - 1, y))  # 상
			if isValidPos(x + 1, y):
				stack.push((x + 1, y))  # 하
			if isValidPos(x, y - 1):
				stack.push((x, y - 1))  # 좌
			if isValidPos(x, y + 1):
				stack.push((x, y + 1))  # 우
		for i in range(stack.size()):
			print(stack.top[i],end='')
		print()
	return False

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

MAX_SIZE = 6

result = DFS()
if result:
	print(' --> 미로탐색 성공')
else:
	print(' --> 미로탐색 실패')
"""

"""
def precedence(op):
	if op == '(' or op == ')': 
		return 0
	elif op == '+' or op == '-': 
		return 1
	elif op == '*' or op == '/': 
		return 2
	else: 
		return -1


def evalPostfix(expr):
	s=Stack()
	for token in expr:
		if token in "+-*/":
			val2=s.pop()
			val1=s.pop()
			if (token=='+'):
				s.push(val1+val2)
			elif(token=='-'):
				s.push(val1-val2)
			elif(token=='*'):
				s.push(val1*val2)
			elif(token=='/'):
				s.push(val1/val2)
		else:
			s.push(float(token))
	return s.pop()



expr1=['8','2','/','3','-','3','2','*','+']
expr2=['1','2','/','4','*','1','4','/','*']

print(expr1,'-->',evalPostfix(expr1))
print(expr2,'-->',evalPostfix(expr2))

def Infix2Postfix(expr):
	s = Stack()
	output = []
	for term in expr:
		if term == '(':
			s.push(term)
		elif term == ')':
			while not s.isEmpty():
				op = s.pop()
				if op == '(':
					break
				else:
					output.append(op)
		elif term in "+-*/":
			while not s.isEmpty() and precedence(term) <= precedence(s.peek()): 
				output.append(s.pop())
			s.push(term)
		else:
			output.append(term)
	while not s.isEmpty():
		output.append(s.pop())
	return output






infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
print(postfix1)
print(postfix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)
print('중위표기 : ', infix1)
print('후위표기 : ', postfix1)
print('중위표기 : ', infix2)
print('후위표기 : ', postfix2)

		
		
"""


		
"""	
def checkBrackets(statement):
	stack=Stack()
	for ch in statement:
		if ch in ('{','[','('):
			stack.push(ch)
		elif ch in ('}',']',')'):
			if stack.isEmpty():
				return False
			else:
				left = stack.pop()
				if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
					return False
	return stack.isEmpty()


str=("{a[(i+1)]}=0;}","if((i==0)&&j==0)","a[(i+1])=0;")
for s in str:
	m=checkBrackets(s)
	print(s,"--->",m)
"""