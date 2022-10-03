# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:24:39 2022

@author: Amanda
"""

# Variable Operations Exercises
sub_code = "sub"
subnr_int = 2
subnr_str = "2"
# Output "sub2" - See below
print(sub_code + subnr_str)
# 1. Both won't work because you can't add a string and a interger together.
# 2. See below
print(sub_code + " " + subnr_str)
print(sub_code + " " + subnr_str * 3)
print((sub_code + subnr_str)* 3)
print((sub_code * 3) + (subnr_str * 3))

# List Operations Exercises
# 1. Create [1, 2, 3] numlist and multiply by 2
numlist = [1, 2, 3]
print(numlist * 2)
# Create [1, 2, 3] numarr and multiply by 2
import numpy as np
numarr = np.array([1, 2, 3])
print(numarr * 2)
# 2. - Multiplying lists duplicates the whole list. 
#    - Multiplying arrays, multiplies each item in the array.
# Create ['do','re','mi','fa'] called "strlist"
strlist = ['do','re','mi','fa']
# 3. See below (Use [0], [-1], [:] etc.)
print([strlist[0] * 2, strlist[1] * 2, strlist[2] * 2, strlist[3] * 2])
print(strlist * 2)
print([strlist[0], strlist[0],
       strlist[1], strlist[1],
       strlist[2], strlist[2],
       strlist[3], strlist[3]])
print([[strlist[0], strlist[0]],
       [strlist[1], strlist[1]],
       [strlist[2], strlist[2]],
       [strlist[3], strlist[3]]])

# Zipping Exercises
imgs_f = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 10 + ['face5.png'] * 5
imgs_h = ['house1.png'] * 5 + ['house2.png'] * 5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5
cues = ['cue1'] * 50 + ['cue2'] * 50
first_item = []
first_item.extend(imgs_f)
first_item.extend(imgs_h)
first_item.extend(imgs_f)
first_item.extend(imgs_h)
imgs_fs = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 5
imgs_hs = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 5
second_item = []
second_item.extend(imgs_hs)
second_item.extend(imgs_fs)
second_item.extend(imgs_hs)
second_item.extend(imgs_fs)
catimgs = list(zip(first_item, second_item, cues))
np.random.shuffle(catimgs)
print(catimgs)
print(len(catimgs))

# Indexing Exercises
# 1. Create a list of colours
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# 2. Print the penultimate colour.
print(colours[-2])
# 3. Print the 3rd and 4th characters of the penultimate colour.
print(colours[-2][2], colours[-2][3])
# 4. Remove purple and add "indigo" and "violet" to the list instead.
colours[-1] = 'indigo'
colours.append('violet')
print(colours)

# Slicing Exercises
# 1. Create a list called list100 with numbers from 0-100
list100 = list(range(101))
print(list100)
# 2. Print the first 10 numbers in the list.
print(list100[:11])
# 3. Print all the odd numbers in the list backwards.
templist100 = list100[1::2]
print(templist100[::-1])
# 4. Print the last four numbers in the list backwards.
temp2list100 = list100[-4:]
print(temp2list100[::-1])
# 5. Are the 40th-44th numbers in the list equal to integers 39-43? Yes
print(list100[39:44] == [39, 40, 41, 42, 43])
