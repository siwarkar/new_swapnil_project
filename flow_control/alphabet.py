"""
==============================
# alphabates
========================
for i in range(1,6):
    print(chr(i+64) *i)
------------------
A
BB
CCC
DDDD
EEEEE
=====================
for i in range(1,6):
    print(chr(70-i)*i)
-----------------------
E
DD
CCC
BBBB
AAAAA
==========================
AAAAA
BBBB
CCC
DD
E
=====================\
for i in range(5,0,-1):
    print(i*chr(70-i))
===================
for i in range(1,6):
    print(chr(i+64)*(6-i))
-------------------------------------
program to print following pattern
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
JJJJJJJJJJ
KKKKKKKKKKK
LLLLLLLLLLLL
MMMMMMMMMMMMM
NNNNNNNNNNNNNN
OOOOOOOOOOOOOOO
PPPPPPPPPPPPPPPP
QQQQQQQQQQQQQQQQQ
RRRRRRRRRRRRRRRRRR
SSSSSSSSSSSSSSSSSSS
TTTTTTTTTTTTTTTTTTTT
UUUUUUUUUUUUUUUUUUUUU
VVVVVVVVVVVVVVVVVVVVVV
WWWWWWWWWWWWWWWWWWWWWWW
XXXXXXXXXXXXXXXXXXXXXXXX
YYYYYYYYYYYYYYYYYYYYYYYYY
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
program type 1
for i in range(1,27):
    print(chr(i+64)*(0+i))
    i+=1
=======================================================================================================
type 2
for i in range(1,0,-1):
    for j in range(1,27):
     print(chr(j+64)*(0+i))
     i+=1
print("")
------------------------------------------------------------
type 3
for i in range(0,1):
    for j in range(1,2):
        for k in range(0,27):
            print(chr(i+64)*(0+i))
            i+=1
print("")

===============================================================================================
print pattern
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
YYYYYYYYYYYYYYYYYYYYYYYYY
XXXXXXXXXXXXXXXXXXXXXXXX
WWWWWWWWWWWWWWWWWWWWWWW
VVVVVVVVVVVVVVVVVVVVVV
UUUUUUUUUUUUUUUUUUUUU
TTTTTTTTTTTTTTTTTTTT
SSSSSSSSSSSSSSSSSSS
RRRRRRRRRRRRRRRRRR
QQQQQQQQQQQQQQQQQ
PPPPPPPPPPPPPPPP
OOOOOOOOOOOOOOO
NNNNNNNNNNNNNN
MMMMMMMMMMMMM
LLLLLLLLLLLL
KKKKKKKKKKK
JJJJJJJJJJ
IIIIIIIII
HHHHHHHH
GGGGGGG
FFFFFF
EEEEE
DDDD
CCC
BB
A
--------------------------------
program
    for i in range(26,0,-1):
    print(chr(i+64)*(0+i))
    i+=1
    ===========================================================================
    print pattern
    A
AA
AAA
AAAA
AAAAA
AAAAAA
AAAAAAA
AAAAAAAA
AAAAAAAAA
-------------------------------------
program
for i in range(0,1):
    for j in range(1,2):
        for k in range(0,10):
            print(chr(j+64)*(0+k))
            i+=1
print("")
================================================================
print pattern
9
88
777
6666
55555
444444
3333333
22222222
111111111
----------------------------------------
program
for i in range(0,1):
    for j in range(1,2):
        for k in range(0,10):
            print(chr(i+58)*(0+k))
            i-=1
            j-=1
            k-=1
print("")
======================================================================


"""

for i in range(0,1):
    for j in range(1,2):
        for k in range(0,10):
            print(chr(j+64)*(0+k))
            i+=1
print("")