""" write a program to reverse the string by using slicing
program:
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
for i in s.split()[::-1]:
    print(i, end=' ')
    output:
    Amitabh Bachchan
    Bachchan Amitabh
============================================================================
# write a program to reverse the each word in string
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
for i in range(-1,-len(s)+1,-1):
    print(s[i])
================================================================
second method
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
#print(s[::-1])
p = reversed(s)
#print(list[p])
empty = ''
for i in reversed(s):
    p = empty.join(i)
    print(p, end='')
===============================================
write a python program Reverse the character of individual word
program
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
s = s.split()
print("splited string is=",s)
for i in s:
    print(i[::-1], end=' ')
===================================================================
example i want to fetch vowels from the string: a,i,o,u,e in s = 'Amitabh Bachchan'
program
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
vowel =('a','e','i','o','u','A','E','I','O','U')
for i in s:
    if (i in vowel):
        print(i, end=' ')
===================================================================
# Interview q. i want a dict of each block and its count
#  {'A':1,'m':1,'i':1,'t':1,'a':3.....}
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
p = {}
for i in s:

    p[i] = s.count(i)
print(p, end='')
=======================================================================
# Print the +ve and -ve index of each block s = 'Amitabh Bachchan'
# example: A is present at 0,-16

s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
length_s = len(s)
for start_latter, poitive_index in zip(s, range(length_s)):
     if start_latter == None:
         pass
     print(start_latter, poitive_index, -length_s)
     length_s = length_s-1
================================================================================
# Interview q. interchange 1st and last 2 chacters from string
# Expected: 'hantabh BachcAmi'
s = 'Amitabh Bachchan'
program
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
for i in s :
    if(len(s) > 2):
     pass
print(s[-4:-1]+s[3:-3]+s[0:3])
# a = s[0:3]
     # b = s[-4:-1]
     #  c = s[3:-3]
#print(b+c+a,end='')
==================================================================
# my key  =3
# means i want to shift characters by 3
# input  s = 'Amitabh Bachchan'
# Expected: Dplwdek#Edfkfkdq
*************program*****************
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
for i in s:
   shifting_char = chr(ord(i)+3)
   print(shifting_char,end='')
=============output==========================
Amitabh Bachchan
Dplwdek#Edfkfkdq
==================================
s = str(input('enter the string= '))
# print('Amitabh Bachchan')
for i in s:
   shifting_char = chr(ord(i)+3)
   print(shifting_char,end='')
   ===================================================
"""
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')









