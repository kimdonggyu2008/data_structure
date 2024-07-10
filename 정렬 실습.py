학과 : 컴퓨터전자시스템공학과
학번 : 201800615 
이름 : 김동규

1. 선택정렬, 삽입정렬, 버블정렬 계산 및 과정 출력

코드
import sys

def printStep(arr,val):
	print("step %2d="%val,end="")
	print(arr)

def selection_sort(A):
	print("선택정렬")
	n=len(A)
	for i in range(n-1):
		least=i
		for j in range(i+1,n):
			if(A[j]<A[least]):
				least=j
		A[i],A[least]=A[least],A[i]
		printStep(A,i)
		

	
def insertion_sort(A):
	print("삽입정렬")
	n=len(A)
	for i in range(1,n):
		key=A[i]
		j=i-1
		while j>=0 and A[j]>key:
			A[j+1]=A[j]
			j-=1
		A[j+1]=key
		printStep(A,i)
		
def bubble_sort(A):
	print("버블정렬")
	n=len(A)
	for i in range(n-1,0,-1):
		bChanged=False
		for j in range(i):
			if(A[j]>A[j+1]):
				A[j],A[j+1]=A[j+1],A[j]
				bChanged=True
		
		if not bChanged:
			break
		printStep(A,n-i)

		
		


while True:
	select=int(input("1:선택정렬 2:삽입정렬 3.버블정렬 4.종료 :"))
	data = [ 5, 3, 8, 4, 9, 1, 6 ,2, 7 ]
	if select==1:
		print("오리지널 : ",data)
		selection_sort(data)
	elif select==2:
		print("오리지널 : ",data)
		insertion_sort(data)
	elif select==3:
		print("오리지널 : ",data)
		bubble_sort(data)
	elif select==4:
		print("종료합니다")
		sys.exit()
	else:
		print("잘못선택했습니다")
	print()
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		

































2. 리스트를 이용한 순차탐색 맵 구현 및 실행
코드
class Entry:
	def __init__(self,key,value):
		self.key=key
		self.value=value
		
	def __str__(self):
		return str("%s:%s"%(self.key,self.value))

def sequential_search(A,key,low,high):
	for i in range(low,high+1):
		if A[i].key==key:
			return i
	return None
	
class SequentialMap:
	def __init__(self):
		self.table = []

	def size(self):
		return len(self.table)

	def display(self, msg):
		print(msg)
		for entry in self.table:
			print(" ", entry)

	def insert(self, key, value):
		self.table.append(Entry(key, value))

	def search(self, key):
		pos = sequential_search(self.table, key, 0, self.size() - 1)
		if pos is not None:
			return self.table[pos]
		else:
			return None

	def delete(self, key):
		for i in range(self.size()):
			if self.table[i].key == key:
				self.table.pop(i)
				return


map = SequentialMap()
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장: ")

print("탐색:game --> ", map.search('game'))
print("탐색:over --> ", map.search('over'))
print("탐색:data --> ", map.search('data'))

map.delete('game')
map.display("나의 단어장: ")

결과





















3. 체이닝을 이용한 해시맵 구현 및 실행
코드
class Node:
	def __init__(self,item,link=None):
		self.data=item
		self.link=link
		
class HashChainMap:
	def __init__(self,M):
		self.table=[None]*M
		self.M=M
		
	def hashFn(self,key):
		sum=0
		for c in key:
			sum=sum+ord(c)
		return sum%self.M
	
	
	def display(self,msg):
		print(msg)
		for idx in range(len(self.table)):
			node=self.table[idx]
			if node is not None:
				print("[%2d]->"%idx,end='')
				while node is not None:
					print(node.data,end='->')
					node=node.link
				print()
				
	def search(self,key):
		idx=self.hashFn(key)
		node=self.table[idx]
		while node is not None:
			if node.data.key==key:
				return node.data
			node=node.link
		return None
	
	def insert(self,key,value):
		idx=self.hashFn(key)
		self.table[idx]=Node(Entry(key,value),self.table[idx])
		
	def delete(self,key):
		idx=self.hashFn(key)
		node=self.table[idx]
		before=None
		while node is not None:
			if node.data.key==key:
				if before==None:
					self.table[idx]=node.link
				else:
					before.link=node.link
				return
			before=node
			node=node.link
			
map=HashChainMap(13)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형탐색')
map.insert('game', '게임')
map.insert('binary search', '이진탐색')
map.display("나의 단어장:")

print("탐색 game ->", map.search('game'))
print("탐색 over ->", map.search('over'))
print("탐색 data ->", map.search('data'))

map.delete('game')
map.display('나의 단어장:')











결과



4. 선형조사법을 이용한 해시맵 구현 및 실행

코드
class Entry:
	def __init__(self,key,value):
		self.key=key
		self.value=value
		
	def __str__(self):
		return str("%s:%s"%(self.key,self.value))

def sequential_search(A,key,low,high):
	for i in range(low,high+1):
		if A[i].key==key:
			return i
	return None
	
class SequentialMap:
	def __init__(self):
		self.table = []

	def size(self):
		return len(self.table)

	def display(self, msg):
		print(msg)
		for entry in self.table:
			print(" ", entry)

	def insert(self, key, value):
		self.table.append(Entry(key, value))

	def search(self, key):
		pos = sequential_search(self.table, key, 0, self.size() - 1)
		if pos is not None:
			return self.table[pos]
		else:
			return None

	def delete(self, key):
		for i in range(self.size()):
			if self.table[i].key == key:
				self.table.pop(i)
				return
class Node:
	def __init__(self, item, link=None):
		self.data = item
		self.link = link

class HashChainMap:
	def __init__(self, M):
		self.table = [None] * M
		self.M = M

	def hashFn(self, key):
		sum = 0
		for c in key:
			sum = sum + ord(c)
		return sum % self.M

	def display(self, msg):
		print(msg)
		for idx in range(len(self.table)):
			node = self.table[idx]
			if node is not None and node.data != ".":
				print("[%2d]->" % idx, end='')
				while node is not None and node.data != ".":
					print(node.data, end='->')
					node = node.link
				print()

	def search(self, key):
		idx = self.hashFn(key)
		while self.table[idx] is not None and self.table[idx]!=".":
			if self.table[idx].data.key == key:
				return self.table[idx].data.key
			else:
				idx+=1
		return None

	def insert(self, key, value):
		idx = self.hashFn(key)
		while self.table[idx] is not None and self.table[idx]!=".":
			idx+=1
		if self.table[idx] is None or self.table[idx] == ".":
			self.table[idx] = Node(Entry(key, value), self.table[idx])

	def delete(self, key):
		idx = self.hashFn(key)
		before = None
		while self.table[idx] is not None and self.table[idx] != ".":
			if self.table[idx].data.key == key:
				if before is None:
					self.table[idx] = self.table[idx].link
				else:
					before.link = self.table[idx].link
				self.table[idx]=None

				return
			before = self.table[idx]
			idx+=1

			
			
map=HashChainMap(13)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형탐색')
map.insert('game', '게임')
map.insert('binary search', '이진탐색')

map.display("나의 단어장:")

print("탐색 game ->", map.search('game'))
print("탐색 over ->", map.search('over'))
print("탐색 data ->", map.search('data'))



map.delete('game')
map.display('game 삭제후 나의 단어장:')

map.delete('over')
map.display('over 삭제후 나의 단어장:')

map.insert('binary','바이너리')
map.display('binary 추가 후 나의 단어장:')