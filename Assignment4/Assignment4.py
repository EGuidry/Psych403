# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:55:52 2022

@author: Amanda
"""

#Conditional Exercises
# 1. See below
response = "NaN"

if response == 1 or response == 2:
    print("OK")
elif response == "NaN":
    print("subject did not respond")
else:
    print("subject pressed the wrong key")
# 2. See below
response = 1

if response == 1 or response == 2:
    if response == 1:
        print("Correct!")
    if response == 2:
        print("Incorrect!")
elif response == "NaN":
    print("subject did not respond")
else:
    print("subject pressed the wrong key")
# 3. Yes it does

#For Loop Exercises
# 1. See below
myName = "Amanda"

for letter in myName:
    print(letter)
# 2. See Below
myName = "Amanda"
counter = -1

for letter in myName:
    counter = counter + 1
    print(letter)
    print(counter)
# 3. List of names and nested loop
names = ["Amy", "Rory", "River"]

for name in names:
    print(name)
    for letter in name:
        print(letter)
# 4. Add counter to list of names
names = ["Amy", "Rory", "River"]

for name in names:
    print(name)
    lettercounter = -1
    
    for letter in name:
        lettercounter = lettercounter + 1
        print(letter)
        print(lettercounter)

#While loop Exercises
# 1. See below
iteration = 0

while iteration < 20:
    if iteration < 10:
        print("%i, image1.png" %iteration)
    elif iteration < 20:
        print("%i, image2.png" %iteration)
        
    iteration = iteration + 1
# 2. See below
import random

response = " "
looping = True

while looping:
    response = random.randint(0,10)
    print(response)
    print("shows an image")
    if response == 1 or response == 2:
        looping = False
# 3. Add failsafe to previous loop
import random

response = " "
looping = True
failsafe = 0

while looping:
    response = random.randint(0,10)
    print(response)
    print("shows an image")
    failsafe = failsafe + 1
    
    if response == 1 or response == 2 or failsafe == 5:
        looping = False
        