#1.Variable Declaration and Types
a = 15
b = 12
#declared 2 variables a & b
print (type(a))
print (type(b))
#prints the types of these 2 variables.

#OUTPUT
<class 'int'>
<class 'int'>





#2.Basic Arithmetic Operations
#Addition
a = 6
b = 9
total_sum = a + b
print("The total is: ",total_sum)
#prints the total sum

#subtraction
a = 10
b = 7
total_difference = a - b
print(total_difference)

#Multiplication
a = 3
b = 4
total_result = a * b
print("The result is: ",total_result)

#Division
a = 8
b = 25
total = a / b
print(f"The answer when these 2 are divided is: {total}")

#OUTPUTS

The total is:  15
3
The result is:  12
The answer when these 2 are divided is: 0.32





#3.Using Variables and Type Casting
a = 28
b = 2 
c = a / b  #Created variable c that stores the result of a / b
c = int(c) 
print("The result: ",c)
print(type(c))  #Prints off the value and type of c
c = float(c)    #converts it into float
print(type(c))

#OUTPUT

The result:  14
<class 'int'>
<class 'float'>




#4.Working with Strings
result = "The result of a divided by b is: "
a = 99
b = 7
c = a / b
c= str(c) #converted it into string
print(type(c))
print(c)

#OUTPUT

<class 'str'>
14.142857142857142



#5.Using Comparison Operators
a = 69
b = 11
result = a > b  #This operator compares if a is greater than b
print(result)

result_2 = a == b   #This operator compares if a is equal to b
print(result_2)

#Output

True
False




