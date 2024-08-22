#!/usr/bin/env python
# coding: utf-8
# Write a python code to generate infinite fibonacci series using generator
# 0,1,1,2,3,5,8,13...


def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b, a+b

f=fib()

#run this code it will show the next number

print(next(f))

#tell the number, where you want to stop it

for i in fib():
    if i>100:
        break
    print (i)







