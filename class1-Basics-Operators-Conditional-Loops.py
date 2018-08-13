# print("Hi")

# ctrl s to save 
# ctrl b to execute

# 3 modes of execution : 
# 1 Interactive mode cmd python >>> quit()
# 2 Scripting mode .py dir python filename.py 
# 3 IDE .py ctrl + b

# ctrl / 

# print("Hi")


# Datatypes : 

# mutable : methods to add update and delete the elements
# immutable : no methods to add update and delete 

# 1 int 101 555 3555 immutable  not iterable  
# 2 float 10.25555 45.555 immutable not iterable  
# 3 str ' ' " " """ """ immutable  iterable 
# 4 list [10,20,30,"Python",[100,200,300,400]] => mutable iterable 
# 5 tuple (10,20,30,"Python") =>immutable iterable
# 6 dict {"emp_id":101,"name":"ABC","email":"abc@xyz.com"} mutable iterable 
# 7 set {10,20,30,45,20}  mutable 
# 8 bool True False immutable 

# num1 = 100
# print(type(num1))
# num2 = 200
# num3 = num1 + num2 
# print(num3)


# num1 = "Hi Python"
# print(type(num1))

# num1 = 100
# num2 = 100

# print(id(num1),id(num2))

# 100         100
# num1		num2
# 1001        1005

# num1 = 200
# print(id(num1))
# 100 num2 
# 200 num1

# l = [10,20,30]
# print(id(l))
# l.append(40)
# print(l,id(l))


# object value and identity 

# num1 = num2 = 200
# print(num1,num2)


# num1,num2 = 100,200
# print(num1,num2)
 
# num1,num2 = num2,num1
# print(num1,num2)

# operators :
# 1 Arithmetic operators +,-,*,/,//-floor divison,%,**
# 2 Comparison operators <,>,<=,>=,== ,!=
# 3 Identity operator is is not 
# 4 Membership operator in not  
# 5 logical operators and or not 
# 6 assignment operators =,+=,-=,/=,*=


# print(10 / 3)
# print(10 // 3)
# print(10 ** 10)
# print(10 % 3)

# num1 = 100
# num2 = 100

# print(num1 == num2)
# print(num1 is num2)

# l1 = [10,20,30]
# l2 = [10,20,30]
# print(id(l1),id(l2))

# print(l1 == l2)
# print(l1 is not l2)

# l = [10,20,30,40,50,60]
# print(500 not in l)

# print(1 in [1,0])

# d = {1:1,2:4,3:9,4:9}
# print(4 in d)


# print(not(5 == 5  and 6!=5))

# num1 = 100
# num1 = num1 + 5
# print(num1)

# num1-=5
# print(num1)


# conditional statements 

# if [condition]:
# 	statements
# elif [condition]:
# 	statements
# else:
# 	statements

# num1 = 400
# num2 = 300


# if (num1 > num2):
# 	print("num1 is greater")
# 	print("just another statements")
# 	if num1 % 2==0:
# 		print("num1 is even")
# 	else:
# 		print("Odd")

# elif (num2 > num1):
# 	print("num2 is greater")
# else:
# 	print("both are equal")

# char = "e"

# if char in 'aeiou':
# 	print("Vowel")
# else:
# 	print("Consonent")

# if "Hi":
# 	print("Hi")
# else:
# 	print("Python")

# 2 Loops 
# 1 for 
# 2 while 


# for [userdefined variable] in [iterable datatype]:
# 	statements 

# l = [10,20,30,40,50]
# range(10) 0..... 9
# range(10,50) 10 11 12 ..... 49
# range(10,50,5) 10 15 20 25 ..... 45

# sum = 0
# for value in range(101):
# 	sum = sum + value
# print(sum)


# 1 +2 +3 ==6

# num1 = 50
# sum = 0
# for value in range(1,num1):
# 	if num1 % value == 0:
# 		sum = sum + value

# if sum == num1:
# 	print("Perfect number")
# else:
# 	print("Not a perfect number")

# print(10,20,sep=",",end="\t")
# print("Hi")


# l = [10,20,30,40,50,60,70,80]
# key = 40

# for index,value in enumerate(l):
# 	print(index,value)

# for index,value in enumerate(l):	
# 	if value == key:
# 		print("Element present",index)	
# 		break 
# else:
# 	print("Element not present")

# if flag == 1:
# 	print(True)
# else:
# 	print(False)


# range 
# enumerate 

# break 
# continue

# else :


# syntax :


# while(condition):


# else:

# count = 1
# sum = 0
# while(count <= 20):
# 	sum = sum + count
# 	count+=1
# print(sum)


# l = [70,60,50,40,30,20,10]
# count = 1
# while(count <= len(l)):
# 	for index in range(len(l)-1):
# 		if l[index] > l[index + 1]:
# 			l[index],l[index+1] = l[index+1],l[index]	
# 	count+=1

# print(l)

# num1 = 53 prime no 
# fibo series 1,1,2,3,5,8....20 
# 2 min from list 

# str 
# list 
# dict 
# set 
