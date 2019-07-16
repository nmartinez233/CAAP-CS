pos =eval(input("This program will calculate the nth Fibonacci number. Please input the nth fibonacci number this program will calculate to:"))
if pos == 1 or pos == 2:
	print(1)
first=1
second=1
for count in range(pos-2):	
	temp = second
	second = first + second
	first = temp
print("The",pos,"th Fibonacci number is ",second)
