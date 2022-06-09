"""
# example 1) write a python  program to find maximum between two numbers? take two number from user
a = float(input("enter the first number :"))  # 1st number
b = float(input("enter the second number :"))   # 2nd number
if a > b:    # check the condition
    print("a is greater than b:")
else:
    print("b is greater than a")
---------------------------------------------------------------------------------------------------
example 2) write a python  program to find maximum between three numbers? take three number from user
program
a = int(input("enter the first number = "))
b = int(input("enter the second number = "))
c = int(input("enter the third number = "))
if (a > b) and (a > c):
    print("a is", a, "the greater than", "b =", b, "and c=", c)

elif (b > c):
    print("b is", b, "the greater than", "a =", a, "and c=", c)
else:
    print("c is", c, "the greater than", "a =", a, "and b=", b)
    --------------------------------------------------------------------------------------------------
 example 3: write a python program to check whether the number is negative ,positive or zero
 (input from user)


a = float(input("enter the number to check it is positive,negative,zero = "))
if (a > 0):
    print("enter number is positve =", a)
elif (a < 0):
    print("enter number is negative =", a)
else:
    print("enter numer is zero =", a)
-----------------------------------------------------------------------------------------------------
example 4: write a pytaon program to check whether the number is divisible of 5 or not

a = int(input("enter number is divisible by 5 or not ="))
a = a % 5
if(a==0) :
    print("enter number is divisible by 5 =")
elif(a > 0) or (a < 0):
    print("enter  number is not divisible by 5 ")
--------------------------------------------------------------------------------------------------
example 5: write a python program to check whether number is even Or odd

a = int(input("check the number is even or odd = "))
a = a % 2
if(a == 0):
    print("enter number is even number")
elif (a > 0) or (a < 0):
    print("enter number is odd number")
-----------------------------------------------------------
example 6 write a python program check the year is leap or not
program
year = int(input("enter year is leap year or not = "))
if(year % 400 == 0) and year(year % 100 == 0):
    print(year, "enter year is leap year  ")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "enter year is leap year ")
else:
    print(year, "enter year is not leap year")
------------------------------------------------------------------------------------
example 7 write a python program to check whether a charater is alphabet or not ?
program

char = str(input("enter the character is alphabet or not = "))
if (len(char) == char[0]):
    print("you enter valid charater")
elif(char.isalpha()):
    print("enter character is alphabet")
else:
    print("please enter only one and valid character ,not enter integer or float is not allow")
    print("enter character is not alphabet")
-----------------------------------------------------------------------------------------------------------
example 8 :
write a python program to check the character is vowel or consonant
program
s = 'a','e','i','o','u','A','E','I','O','U'
p = str(input("enter the character to check vowel or consonant = "))
if p in s:
    print("enter character is vowel")
else:
    print("enter character is consonant")

example 9: write a python program to check whether the character is upper case or lower case
program
s = str(input("enter the charater to check the upper case or lower case= "))
if s in s.upper():
    print("enter character is in upper case")
else:
    print("enter the lower case")
----------------------------------------------------------------------------------
example 10:write a program reverse the word'  Ambitba Bachcan'
s= 'Ambitba Bachcan'
for i in s.split()[::-1]:
    print(i, end=' ')
year = int(input("enter year is leap year or not = "))
if(year % 400 == 0) and (year % 100 == 0):
    print(year, "enter year is leap year  ")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "enter year is leap year ")
else:
    print(year, "enter year is not leap year")
    ===============================================
example:11 write a python program to input angle of triangle and check whether triangle is valid
program:
print("enter the three angle of triangle")
a = int(input('angle 1= '))
b = int(input('angle 2= '))
c = int(input('angle 3= '))
total = a+b+c
total_angle = 180
if total==total_angle:
    print("triangle is valid triangle=",total)
else:
    print("triangle is not valid triangle because it is greater than 180")
=================================================================================================
example:12 write a python program to input length of triangle and check whether triangle is valid
program:
    print("enter the three length of triangle")
a = int(input("enter the length 1 = "))
b = int(input("enter the length 2 = "))
c = int(input("enter the length 3 = "))
if(a + b > c) and (b + c > a) and (a + c > b):
    print("enter length of triangle  is valid")
else:
    print("enter length of triangle  is not valid")
====================================================================================
example 13: write a python program to check whether the triangle is equilateral,
isoscale or scalen triangle
program:
print("check whether the triangle is equilateral,iso scale or scalen triangle")
print("enter the three side of triangle")
a = int(input("enter the side 1 = "))
b = int(input("enter the side 2 = "))
c = int(input("enter the side 3 = "))
if(a == b) and (b == c):
    print("triangle is equilateral triangle")
elif(a != b) and (b != c) and (c != a):
    print("triangle  is scalen triangle")
else:
    print("triangle is iso scale triangle")
==========================================================================
program 14: write a python program to calculate profit and loss.
input is selling cost and actual cost
program:
print("*************check the profit and loss***********************")
actual_cost = float(input("enter the actual_cost = "))
selling_cost = float(input("enter the selling_cost = "))
if(actual_cost-selling_cost>0):
   amount = actual_cost-selling_cost
   print("total loss amount={0}".format(amount))
elif(selling_cost - actual_cost >0):
    amount =selling_cost-actual_cost
    print("total profit amount = {0}".format(amount))
else:
    print("no  profit no loss")
==============================================================================
example:15 write a program to input marks of five subject phy,chem,bio,math,comp
calculate percentage and grade
program:
print("************calculate the percentage and grades**************")
phy = int(input("enter the phy marks = "))
chem = int(input("enter the chem marks = "))
bio = int(input("enter the bio marks = "))
math = int(input("enter the math marks = "))
comp = int(input("enter the comp maprks = "))
total = phy+chem+bio+math+comp
print("total mark is =",total)
percentage = total/5
print("percentage is=",percentage)
if(percentage >= 90):
 print("congratulation you will get 'A GRADE'and percentage = ", percentage)
if(percentage >= 80) and (percentage < 90):
 print("congratulation you will get 'B GRADE'and percentage = ", percentage)
if(percentage >= 70) and (percentage < 80):
 print("congratulation you will get 'C GRADE'and percentage = ", percentage)
if (percentage >= 60) and (percentage < 70):
 print("congratulation you will get 'D GRADE'and percentage = ", percentage)
if (percentage >= 35) and (percentage < 60):
 print("congratulation you will get 'E GRADE'and percentage = ", percentage)
if (percentage < 35):
 print("sorry!!!!!! you are 'FAIL'and percentage = ", percentage)
===============================================================================================
program 16: write a python program to input basic python salary of an employee and calculate its gross salary
according to following
Basic_salary<=10000:HRA=20%,DA=80%
Basic_salary<=20000:HRA=30%,DA=90%
Basic_salary>10000:HRA=35%,DA=95%
program:
print("********Calculate the GROSS SALARY**********")
Basic_salary = float(input("enter the Basic_Salary = "))
if (Basic_salary <= 10000):
   HRA = Basic_salary * (20.00 / 100.00)
   DA = Basic_salary * (80.00 / 100.00)
elif(Basic_salary >= 10000) and (Basic_salary <= 20000) :
    HRA = Basic_salary * (30.00 / 100.00)
    DA = Basic_salary * (90.00 / 100.00)
elif(Basic_salary > 20000):
   HRA = Basic_salary * (35.00/100.00)
   DA = Basic_salary * (95.00/100.00)
gross_salary = Basic_salary + HRA + DA

print("The gross salary is =", gross_salary)
=============================================================================
program 17 : Program to Count Total numbers of notes in given amount
*****************************program using if statement *********************************************
amt=int(input("Enter Amount\n"))
note2000=note500=note100=note50=note20=note10=note5=note2=note1=0
if amt>=2000:
    note2000=amt//2000
    amt=amt-note2000*2000
if amt>=500:
    note500=amt//500
    amt=amt-note500*500
if amt>=100:
    note100=amt//100
    amt=amt-note100*100
if amt>=50:
    note50=amt//50
    amt=amt-note50*50
if amt>=20:
    note20=amt//20
    amt=amt-note20*20
if amt>=10:
    note10=amt//10
    amt=amt-note10*10
if amt>=5:
    note5=amt//5
    amt=amt-note5*5
if amt>=2:
    note2=amt//2
    amt=amt-note2*2
if amt>=1:
    note1=amt//1
    amt=amt-note1*1
print("2000 =",note2000)
print("500= ",note500)
print("100= ",note100)
print("50= ",note50)
print("20 =",note20)
print("10 =",note10)
print("5 =",note5)
print("2= ",note2)
print("1 =",note1)
*****************************program using if statement 2 *********************************************
amt = int(input("given amount :"))
if amt >= 2000:
 note2000 = amt //2000
 amt = amt % 2000
 print("given amount have notes of :\nnote 2000=",note2000)
if amt >= 500:
 note500 = amt //500
 amt = amt % 500
 print("note 500=", note500)
if amt >= 200:
 note200 = amt // 200
 amt = amt % 200
 print("note 200=", note200)
if amt >= 100:
 note100 = amt //100
 amt = amt % 100
 print("note 100=", note100)
if amt >= 50:
 note50 = amt // 50
 amt = amt % 50
 print("note 50=", note50)
if amt >= 20:
 note20 = amt // 20
 amt = amt % 20
 print("note 20=", note20)
print("coins=",amt)
*****************************program  using loop *********************************************
notes = (2000,500,200,100,50,20,10,5,2,1)
amount = int(input("Enter Amount to be paid := "))
for C in notes:
    count = amount//C
    print("Note Value : ", C,'\tnumber of notes ',count)
    amount = amount%C
====================================================================
example 18 write a program input electricity unit charge and calculate total
electric bill according to given condition
For first 50 units Rs.0.50/unit,
For next 100 units Rs.0.75/unit,
 For next 100 units Rs.1.25/unit,
 For above 250 units Rs.1.50/unit.
An Additional surcharge of 17% is added  to the bill
program*****************
type 1:
print ("*********************** Electric bill system *****************")
unit = int(input("Please enter valid unit = "))
if unit <= 0:
    pay = 0
    pass
elif(unit >= 1) and (unit <= 50):
    charge = unit * 0.50
    additional_tex = charge /100 *17
    pay =charge + additional_tex
elif unit <= 100:
    charge = (50 * 0.50) + (unit - 50) * 0.75
    additional_tex = charge / 100 * 17
    pay = charge + additional_tex
elif unit <= 250:
    charge = (50 * 0.50) + (100 - 50) * 0.75 + (unit - 100) * 1.25
    additional_tex = charge / 100 * 17
    pay = charge + additional_tex
elif unit > 250 :
    charge = (50 * 0.50) + (100 - 50) * 0.75 + (250 - 100) * 1.25 + (unit - 250) * 1.50
    additional_tex = charge / 100 * 17
    pay = charge + additional_tex
else:
    pay = 0
print ("You are consuming {} unit and you want to pay {} bill".format(unit,pay),"\n!!!!!!!!! Thanks you !!!!!!!!! ")
===============================================================================

    """




