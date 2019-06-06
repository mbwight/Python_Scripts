__author__ = 'Mark'
n = int(input("Enter a positive integer: "))
m = int(input("Enter another positive integer"))
while n != 0:
    t = n
    n = m % n
    m = t
if n == 0:
    print ("The greatest common divisor is", m)

