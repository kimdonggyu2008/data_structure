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