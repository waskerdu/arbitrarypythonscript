# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:56:09 2017

@author: Riley
"""
#assign int
myInt=4
#assign string
myString="strings are stringy"
#assign float
myFloat=4.0
#print stuff
print (myFloat)
#use math stuff
print (myInt+myFloat)
print (myInt-myFloat)
print (myInt*myFloat)
print (myInt/myFloat)
#use more math stuff
myInt+=1
myInt=int(myFloat+1)
isEven=myInt%2
#conditionals
if isEven==0:
    print ("is even")
elif isEven==1:
    print ("is odd")
else:
    print ("how did that happen?")
def isEven(x):
    return (x%2)==0
#more conditional stuff
if isEven(2) and isEven(4):
    print ("math still works!")
if isEven(2) or isEven(3):
    print ("2 is even but three is not")
if isEven(2) and (not isEven(3)):
    print ("see above")
#while loops
while True:
    if isEven(2):
        print("better exit this loop")
        break
#for loops
for number in range(10):
    if isEven(number):
        print (str(number)+" is even")
    else:
        print (str(number)+" is odd")
#iterate through list
myList=[1,2,3,4,5]
for number in myList:
    print (number)
#iterate through tuple
myTuple=tuple(myList)
for number in myTuple:
    print (number)
#make a function that returns strings
def stringReturner():
    return "spam and eggs"
#print it
print (stringReturner())