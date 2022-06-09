"""
example 1 : write a python program to print the following string in a specific format
"Twinkle,twinkle ,little star, How I wonder what you are! Up above the world so high,
like a diamond in the sky.Twinkle,twinkle, little star,How I wonder what you are!"

program code:
print('Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\tUp above the world so high, \n\t\t\tLike a '
      'diamond in the sky.\n\t\t\t\tTwinkle,twinkle, little star,\n\t\t\t\t\t How I wonder what you are!')
***********output:
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle,twinkle, little star,
How I wonder what you are!
-------------------------------------------------------------------------------------------------------------------
example 2: write a python program to get the python version you are  using
program code
import sys
print('python version')
print(sys.version)
print('python version info')
print(sys.version_info)
****output****
python version
3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
python version info
sys.version_info(major=3, minor=10, micro=4, release level='final', serial=0)
--------------------------------------------------------------------------------------------------------
example 3: write python program to display the current date and time

import datetime
now =datetime.datetime.now()
print('current date and time :')
print(now)
print(now.strftime('%y/%m/%d%H:%M:%S'))
------------------------------------------------------------------------------
EXAMPLE 4:WRITE A PROGRAM WHICH ACCEPT THE RADIUS OF A CIRCLE FROM USER AND COMPUTE THE AREA

from math import pi
rad = float(input("enter the radius of circle:"))
area = pi*rad**2
print("area of the circle=",area)
-----------------------------------------------------------------------------------------------
EXAMPLE 5: WRITE A PYTHON PROGRAM WHICH ACCEPT THE USER FIRST NAME  AND LAST NAME AND PRINT THEM IN REVERSE ORDER
 WITH A SPACE BETWEEN THEM
 program code:
first_name = input("enter the first name:")
last_name = input("enter the last name:")
print('hello ' + last_name + " " + first_name)
-------------------------------------------------------------------------------------------------------
"""
s = '190'
print(complex(int(s)))
print(bytes(int(s)))
print(bytearray(int(s)))
print(float(int(s)))

