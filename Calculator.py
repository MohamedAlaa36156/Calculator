while (1):
	print("Welcome To ITI Calculator")
	mode=int(input("(1)For Logical Calculator Enter:\n(2)For Scientific Calculator Enter:\n(3) To Exit The Application\n "))
	result=0
	if ( mode == 1):
		num1=int(input("Please enter 1st Number : "))
		num2=int(input("Please enter 2nd Number : "))
		operation=input("Please Enter the Operation'+,-,*,/,&,|,~,^,(>>,<<) Shift 1st by 2nd ' :   ")
		if operation == '+':
			result=num1+num2
			print("Number 1 + Number 2 = ",bin(result))
			print("Number 1 + Number 2 = ",hex(result))
			print("Number 1 + Number 2 = ",oct(result))
	
		elif operation == '-':
			result=num1-num2
			print("Number 1 - Number 2 = ",bin(result))
			print("Number 1 - Number 2 = ",hex(result))
			print("Number 1 - Number 2 = ",oct(result))
		elif operation == '*':
			result=num1*num2
			print("Number 1 * Number 2 = ",bin(result))
			print("Number 1 - Number 2 = ",hex(result))
			print("Number 1 - Number 2 = ",oct(result))
		elif operation == '/':
			result=num1/num2
			print("Number 1 / Number 2 = ",bin(result))
			print("Number 1 - Number 2 = ",hex(result))
			print("Number 1 - Number 2 = ",oct(result))
		elif operation == '&':
			result=num1&num2
			print("Number 1 & Number 2 = ",bin(result))
			print("Number 1 - Number 2 = ",hex(result))
			print("Number 1 - Number 2 = ",oct(result))
		elif operation == '|':
			result=num1|num2
			print("Number1 | Number 2 = ",bin(result))
			print("Number 1 - Number 2 = ",hex(result))
			print("Number 1 - Number 2 = ",oct(result))
		elif operation == '~':
			result=~num1
			print("!Number 1 = ",bin(result))
			print("!Number 1 = ",hex(result))
			print("!Number 1 = ",oct(result))
			result=~num2
			print("!Number 2 = ",bin(result))
			print("!Number 2 = ",hex(result))
			print("!Number 2 = ",oct(result))
		elif operation == '^':
			result=num1^num2
			print("Number 1 ^ Number 2 = ",bin(result))
			print("Number 1 ^ Number 2 = ",hex(result))
			print("Number 1 ^ Number 2 = ",oct(result))
		elif operation == '<<':
			result=num1<<num2
			print("Number 1 << Number 2 = ",bin(result))
			print("Number 1 << Number 2 = ",hex(result))
			print("Number 1 << Number 2 = ",oct(result))
		elif operation == '>>':
			result=num1>>num2
			print("Number 1 >> Number 2 = ",bin(result))
			print("Number 1 >> Number 2 = ",hex(result))
			print("Number 1 >> Number 2 = ",oct(result))
		else:
			print("Wrong Entry")
	elif (mode == 2):
		num1=int(input("Please enter 1st Number : "))
		num2=int(input("Please enter 2nd Number : "))
		operation=input("Please Enter the Operation'+ , - , * , / , % ' : ")
		if operation == '+':
			result=num1+num2
			print("Number1 + Number 2= ",(result))
		elif operation == '-':
			result=num1-num2
			print("Number1 - Number 2= ",(result))
		elif operation == '*':
			result=num1*num2
			print("Number1 * Number 2= ",(result))
		elif operation == '/':
			result=num1/num2
			print("Number1 / Number 2= ",(result))
		elif operation == '%':
			result=num1%num2
			print("Number1 % Number 2= ",(result))
	elif mode==3:
		break;
	else:
		print("Wrong Entry please retry")
	