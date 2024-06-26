import random
dop=random.randint(0,100)

def compare_answer(inputted):
	global dop
	if inputted<dop:
		return 1
	elif inputted==dop:
		return 0
	elif inputted>dop:
		return -1
	

answers=["아닙니다. 더 작은 숫자입니다","정답입니다","아닙니다 더 큰 숫자입니다"]
for i in range(10):
	inputted=int(input("두자리 정수 입력"))
	result=compare_answer(inputted)
	result+=1
	if(result!=1):
		print(answers[result])
	else:
		print(answers[result], i,"번만에 맞추셨습니다")
		break
print("게임끝!")