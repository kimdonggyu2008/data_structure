

코드
MAX_QSIZE=10
class CircularQueue:
	def __init__(self):
		self.front=0
		self.rear=0
		self.items=[None]*MAX_QSIZE
	
	def isEmpty(self):
		return self.front==self.rear
	
	def isFull(self):
		return self.front==(self.rear+1)%MAX_QSIZE
	
	def clear(self):
		self.front=self.rear
	
	def enqueue(self,item):
		if not self.isFull():
			self.rear=(self.rear+1)%MAX_QSIZE
			self.items[self.rear]=item
	
	def dequeue(self):
		if not self.isEmpty():
			self.front=(self.front+1)%MAX_QSIZE
			return self.items[self.front]
	
	def peek(self):
		if not self.isEmpty():
			return self.items[(self.front+1)%MAX_QSIZE]
	
	def size(self):
		return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
	
	def display(self):
		out = []
		if self.front < self.rear:
			out = self.items[self.front+1:self.rear+1]
		else:
			out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
		print("[f=%s, r=%d] => " % (self.front, self.rear), out)
	
	

class TNode:
	def __init__(self,data,left,right):
		self.data=data
		self.left=left
		self.right=right
		

def preorder(n):
	if n is not None:
		print(n.data,end=' ')
		preorder(n.left)
		preorder(n.right)
		
def inorder(n):
	if n is not None:
		inorder(n.left)
		print(n.data,end=' ')
		inorder(n.right)
		
def postorder(n):
	if n is not None:
		postorder(n.left)
		postorder(n.right)
		print(n.data,end=' ')
		
		
def levelorder(root):
	queue=CircularQueue()
	queue.enqueue(root)
	while not queue.isEmpty():
		n=queue.dequeue()
		if n is not None:
			print(n.data,end=' ')
			queue.enqueue(n.left)
			queue.enqueue(n.right)
		
def count_node(n):
	if n is None:
		return 0
	else:
		return 1+count_node(n.left)+count_node(n.right)
	
def count_leaf(n):
	if n is None:
		return 0
	elif n.left is None and n.right is None:
		return 1
	else:
		return count_leaf(n.left)+count_leaf(n.right)

def calc_height(n):
	if n is None:
		return 0
	hLeft=calc_height(n.left)
	hRight=calc_height(n.right)
	if (hLeft>hRight):
		return hLeft+1
	else:
		return hRight+1
		
d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('\n In-Order : ', end='')
inorder(root)
print('\n Pre-Order : ', end='')
preorder(root)
print('\n Post-Order : ', end='')
postorder(root)
print('\nLevel-Order : ', end='')
levelorder(root)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 단말의 개수 = %d개" % count_leaf(root))
print(" 트리의 높이 = %d" % calc_height(root))

결과
		










2. 모스 부호 구현 및 실행

코드
		
table = [	('A', '.-'),	('B', '-...'),	('C', '-.-.'),	('D', '-..'),	('E', '.'),	('F', '..-.'),	('G', '--.'),	('H', '....'),	('I', '..'),	('J', '.---'),	('K', '-.-'),	('L', '.-..'),	('M', '--'),	('N', '-.'),	('O', '---'),	('P', '.--.'),	('Q', '--.-'),	('R', '.-.'),	('S', '...'),	('T', '-'),	('U', '..-'),	('V', '...-'),	('W', '.--'),	('X', '-..-'),	('Y', '-.--'),	('Z', '--..')]
		

def make_morse_tree():
	root =TNode(None,None,None)
	for tp in table:
		code=tp[1]
		node=root
		for c in code:
			if c=='.':
				if node.left==None:
					node.left=TNode(None,None,None)
				node=node.left
			elif c=='-':
				if node.right==None:
					node.right=TNode(None,None,None)
				node=node.right
				
		node.data=tp[0]
	return root

def encode(ch):
	idx=ord(ch)-ord('A')
	return table[idx][1]

def decode(root,code):
	node=root
	for ch in code:
		if ch=='.':
			node=node.left
		elif ch=='-':
			node=node.right
	return node.data

morseCodeTree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
	code = encode(ch)
	mlist.append(code)
print("Morse Code: ", mlist)
print("Decoding : ", end='')
for code in mlist:
	ch = decode(morseCodeTree, code)
	print(ch, end='')
print()

결과


3. 힙 구현 및 실행

코드
		
class MaxHeap:
	def __init__(self):
		self.heap=[]
		self.heap.append(0)
		
	def size(self):
		return len(self.heap)-1
	def isEmpty(self):
		return self.size()==0
	def Parent(self,i):
		return self.heap[i//2]
	def Left(self,i):
		return self.heap[i*2]
	def Right(self,i):
		return self.heap[i*2+1]
	def display(self,msg='힙 트리:'):
		print(msg,self.heap[1:])


	def insert(self,n):
		self.heap.append(n)
		i=self.size()
		while(i!=1 and n>self.Parent(i)):
			self.heap[i]=self.Parent(i)
			i=i//2
		self.heap[i]=n

	def delete(self):
		parent=1
		child=2
		if not self.isEmpty():
			hroot=self.heap[1]
			last=self.heap[self.size()]
			while(child<=self.size()):
				if child<self.size() and self.Left(parent)<self.Right(parent):
					child+=1
				if last>=self.heap[child]:
					break;
				self.heap[parent]=self.heap[child]
				parent=child
				child*=2

			self.heap[parent]=last
			self.heap.pop(-1)
			return hroot

heap = MaxHeap()
data = [2, 5, 4, 8, 9, 3, 7, 3]
print("[삽입 연산] :", str(data))

for elem in data:
	heap.insert(elem)

heap.display('[ 삽입 후 ]:')
heap.delete()
heap.display('[ 삭제 후 ]:')
heap.delete()
heap.display('[ 삭제 후 ]:')
		

결과
















