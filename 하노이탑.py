count=0
def hanoi_tower(n,fr,tmp,to):
	global count
	count+=1
	if (n==0):
		return
	if (n==1):
		print("원판1:%s --> %s"%(fr,to))
		return 
	else:
		hanoi_tower(n-1,fr,to,tmp)
		print("원판%d:%s --> %s"%(n,fr,to))
		hanoi_tower(n-1,tmp,fr,to)
		
for i in range(1,5):
	hanoi_tower(i,'A','B','C')
	print("총 횟수",count)
	print("===============")
	count=0
	