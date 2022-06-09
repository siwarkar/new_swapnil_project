"""
example 1: write a python program to print all natural number from 1 to n using while loop
******************program*********************
print("***********Natural Number**********")
natural = int(input("plz enter the number you want print natural number list till given number = "))
for i in range(1, natural+1):
     print(i, end=' ')
=================================================================================================
example 2: write a program in python to print all natural number in reverse(from n to 0)
program
natural = int(input("plz enter the number you want to print in reverse order= "))
i = natural
print(" list of natural number from {0} to 1 in reverse=".format(natural))
while(i>=1):
    print(i, end=' ')
    i-=1
============================================================================
example 3:write a python program to print  all alphabet from a to z using while loop
***using for loop***
print("print the all alphabet a to z")
i = 'a'
for i in range(ord('a'),ord('z')):
    print(chr(i),end=" ")
print("\nprint the all alphabet A to Z")
i = 'A'
for i in range(ord('A'), ord('Z')):
    print(chr(i), end=" ")
********while loop*********
    a = 65
while(a<=90):
    b = chr(a).lower()
    #c = chr(a).upper()
    print("{} ".format(b),end="")
   # print("{} ".format(c), end="")
    a+=1
=========================================================================================
example 4: write a python program to print all even number between 1 to 100 using while loop
program:-
start = 1
max = 100
while(start<=max):
    if(start%2==0):
        print("%d" %(start), end=' ')
    start+=1
=====================================================================================
example 5 write a python program to print all odd number between 1 to 100 using while loop
program:-
start = 1
max = 100
while(start<=max):
    if(start%2!=0):
        print("%d" %(start), end=' ')
    start+=1
============================================================================================
example 6 : write a python program to find sum of all natural number between 1 to n
print("******enter the natural number to get sum of all natural number you given******")
natural = int(input("enter the number till that number you get sum = "))
sum=0
for i in range(1,natural+1):
    sum= sum + i
print("sum of natural number 1 to {} is {}".format(natural,sum))
====================================================================================
example 7:write a python program to find sum of all even number between 1 to n
program:-
print("******enter the number to get sum of all even number you given******")
even = int(input("enter the number till that number you get sum of all even number = "))
sum=0
print("list of even number")
for i in range(1, even+1):
    if(i % 2==0):
        print("{}".format(i),end=" ")
        sum = sum + i
print("\nsum of even number 2 from {} is {}".format(even,sum))
==============================================================================
example 9:write a python program to find sum of all even number between 1 to n
program
print("******enter the number to get sum of all odd number you given******")
odd = int(input("enter the number till that number you get sum of all odd number = "))
sum=0
print("list of odd number")
for i in range(1, odd+1):

    if(i % 2!=0):
        print("{}".format(i),end=" ")
        sum = sum + i
print("\nsum of even number in between 1 to {} is {}".format(odd,sum))
=======================================================================================
example 10:write a python program to print multiplication table of any number take form user
program:-
print("******multiplication table******")
number = int(input("enter the number you want multiplication table of thi number ="))
mul = number
print("print table of given number")
for i in range(1, 11):
        mul =  number * i
        print("{}".format(mul),end=" ")
        #  print("{}   *   {} =   {}".format(i,number,mul))
===========================================================================================================
example 11: write a python program to count the number of digits in a number
program:
************** using while loop************
print("******number of digits in given number******")
number = int(input("enter the number = "))
count = 0
while number != 0:
    number //= 10
    count += 1
print("number of digits in given number = ", count)
*************using  for loop***************
print("******number of digits in given number******")
number = int(input("enter the number = "))
count = len(str(number))
for i in range(1, count-1):
    if(number!=0):
        number//=10
print("number of digits in given number = ", count)
=======================================================================
example 12 : write a python program to find first and last digit of a number.
program:-
*********without loop*************
n = int(input("enter any number : "))
length=str(n)
first_digit = length[0]
last_digit = length[-1]
sum = int(first_digit) + int(last_digit)
print("first digit = ", int(first_digit))
print("last digit  = ", int(last_digit))
print("the sum of {} and {} = {}".format(first_digit,last_digit,sum))
***************using Loop**************
n = int(input("enter any number : "))
last_digit = n % 10
while n>=10:
    n = n // 10
print("first_digit   = ", n)
print("last_digit is = ", last_digit)
==================================================================
example 13 : write a python program to find sum of first and last digit of a number.
program:-
********** using loop ************
print("********* sum of first and last digit of given number ********")
number = int(input("enter any number : "))
last_digit = number % 10
while number>=10:
    number = number // 10
print("first_digit   = ", number)
print("last_digit is = ", last_digit)
sum = number + last_digit
print("sum of {} and {} is = {}".format(number,last_digit,sum))
=====================================================================
example 14 : write a python program to find swap first and last digit of a number.
program:-
print("********* sum of first and last digit of given number ********")
number = int(input("enter any number : "))
last_digit = number % 10
while number>=10:
    number = number // 10
print("first_digit   = ", number)
print("last_digit is = ", last_digit)
temp = number
number = last_digit
last_digit= temp
print("value after swap first_number",number)
print("value after swap last_number",last_digit)
==========================================================================================
example 15 : write a python program to calculate the sum of digits
program:-
print("********* sum of digits in number ***********")
number = str(input("enter the number you want sum of all digits = "))
sum = 0
for i in number:
 sum=sum+int(i)
print("sum of all digits =",int(sum))
==============================================================================
example 16 : write a python program to calculate the product of digits
program
print("********* product of digits in number ***********")
number = str(input("enter the number you want product of all digits = "))
product = 1
for i in number:
 product = product * int(i)
print("product of all digits =",int(product))
===========================================================================================
example 17: write a python program revrse number and print reverse
print("********* reverse digits in number ***********")
number = input("enter the number you want reverse of all digits = ")
print("reverse the number = ", number[::-1])
==================== using loop========================================================
print("********* reverse digits in number ***********")
number = int (input("enter the number you want reverse of all digits = "))
reverse =0
while (number>0):
    Digit =number % 10
    reverse = reverse *  10 + Digit
    number =number // 10
print("reverse the number = ", reverse)
============================================================================================
example 18:-write a python program to check whether a number is palindrome or not
example:
print("********* The number is palindrome or not***********")
number = int(input("enter the number= "))
temp = number
reverse =0
while number > 0:
    Digit = number % 10
    reverse = reverse * 10 + Digit
    number = number // 10
#print("reverse the number = ", reverse)
if temp == reverse:
    print("the number is a palindrome!")
else:
    print("the number isn't a palindrome!")
============================================================================================
example 19: write a program to find frequency of each digit in given integer
program
print("***************************To check the frequency of digits in number***************")
number = int(input("enter the number = "))
print("\nDigit \tFrequency")
for i in range(0,10):
    count = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        if digit == i:
            count = count + 1
        temp = temp // 10
    if count > 0:
        print(i, "\t\t", count)
==============================================================================================
example 20 :-write a python program to enter digit and print in word
program :-
print("***************************digits is convert in word ***************")
number = int(input("enter the number = "))
if number<=255:
    word = ascii(number)
    print(chr(int(word)))
else:
    print("you enter the out of range vale in ascii value")
==============================================================================
example 21:write a python program to find power of a number using for loop
program
print("************power of given number ***************")
base = int(input("enter the base = "))
exponant = str(input("enter the exponant = "))
for i in exponant:
    power = base ** int(exponant)
print("the power of base:{} and exponant:{} = power:{}".format(base,exponant,int(power)))
================================================================================================
example 22 :write a python program to calculate factorial of given number
program
number = int(input("enter the number = "))
print("******** factorial of given number ************")
factorial = 1
if number >= 1:
    for i in range(1, number + 1):
        factorial = factorial * i
print("factorial of number {} is = {}".format(number, factorial))
===========================================================================================
# Recursive function to return hcf of num1 and num 2
def hcf(num1, num2):
    # Everything divides 0
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    # base case
    if num1 == num2:
        return num1

    # a is greater
    if num1 > num2:
        return hcf(num1 - num2, num2)
    return hcf(num1, num2 - num1)


# Driver program to test above function
num1 = int(input("enter the number1 = "))
num2 = int(input("enter the number2 = "))
if (hcf(num1, num2)):
    print('hcf of', num1, 'and', num2, 'is', hcf(num1, num2))
else:
    print('not found')
program:-(incomplete)
number1 = int(input("enter the number1 = "))
number2 = int(input("enter the number2 = "))
print("******** HCF of given number **** ******")
if number1 > number2:
     smaller = number2
  else:
     smaller = number1
    for i in range(1, smaller+1):
        if(number1 % i == 0) and (number2 % i == 0):
          hcf = i
        print(hcf)
==========================================================================================
example 25: write a program to check number is prime number or n
program
number = int(input("enter the number = "))
if number > 1:
    for i in range(2,number):
        if number % i == 0:
            print(number, "is not prime number")
            break
        else:
            print(number,"is a prime number")
            break
else:
         print(number, "is not prime number")
=================================================================================================
example 26: write a program to print prime number in 1 to n

print("******print prime number given in start and end********************")
start = int(input("enter the starting point = "))
end = int(input("enter the ending point = "))
for number in range(start,end+1):
    count =0
    for i in range(2,(number//2+1)):
        if number % i==0 :
           count += 1
           break
    if (count == 0) and (number != 1):
        print(number,end=' ')

==========================================================================================================
example 27 write a program to print  the sum of prime number in 1 to n
program
print("******print prime number given in start and end********************")
start = int(input("enter the starting point = "))
end = int(input("enter the ending point = "))
total = 0
for number in range(start,end+1):
    count =0
    for i in range(2,(number//2+1)):
        if number % i==0 :
           count += 1
           break
    if (count == 0) and (number != 1):
        print(number,end=' ')
        total = total + number
print("\nsum of all prime number {} to {} is = {}".format(start,end,total))
==========================================================================================
Example28: program:write a program to check whether a numer is armstrong number or not
program
print("************** armstrong number or not *****************")
num = int(input('enter the number = '))
sum = 0
temp = num
while temp > 0:
    loop = 1
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    print("*************loop {} times *****************".format(loop))
    print("digit = ",digit)
    print("sum = ",sum)
    print("temp = ",temp)
    print("---------------------------------------------------")
if num == sum:
    print("check it is equql or not")
    print("{} == {}".format(num,sum))
    print("{} is an armstrong number".format(num))
else:
    print("check it is equql or not")
    print("{} != {}".format(num, sum))
    print("{} is not an armstrong number".format(num))
==============================================================================
example29: program:write a program to print armstrong number 1 t0 n.
program
print("************** armstrong number or not *****************")
start = int(input('enter the start = '))
end = int(input('enter the end = '))
if start <= end :
  print("This is your armstrong number in {} between {}".format(start, end))
else:
    print("you should enter starting point is less than end point ")
for num in range(start,end+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
               digit = temp % 10
               sum += digit ** order
               temp //= 10
    if num == sum:
         print(num, end=" ")
=============================================================================================
example 30: write a python program to print fibonacci series up to nnumber
program:
print("************** fibonacci series *****************")
num = int(input("Enter the how many number you want in series = "))
starting = 0
senond = 1
count = 0
if num <= 0:
    print("please enter  positive interger")
elif num == 1 :
    print("fibonacci series upto {}".format(num))
    print(starting)
else:
    print("**************************** fibonacci series:************************")
    while count < num:
        print(starting)
        temp = starting + senond
        starting = senond
        senond = temp
        count+=1
==================================================================================
example 31: write a python program to print following  star pattern
*
* *
* * *
* * * *
* * * * *
program
1)  for i in range(1,6):
    print(i*"*")
2)for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print("")
==============================================================
example 32: write a python program to print following number pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
program:
1)for i in range(1,6):
    for j in range(0,i):
        print(i,end=" ")
    print("")
2)for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print("")

"""
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print("")