#square root

num = 5
sqrt = num * 0.5
print("the sqrt if {} is {}".format(num,sqrt))

#input from user
num=int(input("enter the num:"))
sqrt=num*0.5
print('the sqrt of %0.3f is %0.3f' %(num,sqrt))

# Find square root of real or complex numbers
# Importing the complex math module

import cmath
#num = 1+2j
num = eval(input("enter a complex no:"))
sqrt = cmath.sqrt(num)
print('the sqrt of {0} is {1:0.3f}+{2:0.3f}'%(num,sqrt.real,sqrt.imag))