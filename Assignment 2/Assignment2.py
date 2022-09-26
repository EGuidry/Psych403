# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:02:42 2022

@author: Amanda
"""
# Operations Exercises
print (5/2)
print (5.0/2.0)
# 1. Yes
print (6 % 3)
# 2. It divides the numbers and then prints the remainder.
print (2 ** 4)
# 3. ** is exponential (Ex: 2**4 = 16)
print (101 // 25)
# 3. Continued: // rounds down how much a number goes into another-
# without the remainder (Ex: 110 // 20 = 5)
print (110 // 20)
# 4. No
print (2 + 4 + 3 * 2 / 2)

# Boolean Exercises
print (1 == 1.0)
# 1. 1 and 1.0 are equivalent 
# “1” and “1.0” are not equal because it becomes a string and removes value.
# so it becomes a word.
print ('1' == '1.0')
# 2. Yes
print (5 == (3 + 2))
# 3. See below:
print (1 == 1.0 or '1' == '1.0' and not 5 == (3 + 2))
print (1 == 1.0 and not '1' == '1.0' or 5 == (3 + 2))
print (1 == 1.0 and not '1' == '1.0' and 5 == (3 + 2))
print (1 == 1.0 or '1' == '1.0' and 5 == (3 + 2))
print (1 == 1.0 or '1' == '1.0' or 5 == (3 + 2))

#List Exercises
# 1. Yes it did
oddlist = [1,3,5,7,9]
# 2. See below:
print (oddlist)
print (len(oddlist))
# 3. Five
print (type(oddlist))
# 4. It says <class 'list'>
# 5. See below:
intlist = (list(range(1,100)))
print (intlist)
# 6. Yes it does

# Dictionary Exercises
about_me = {'Name': 'Amanda', 
            'Age': '32.0', 
            'YearOfStudy': '4', 
            'FavouriteFoods': ['Tonkatsu','Cheesecake','Steak'] }
print (about_me)
print (type(about_me))
print (len(about_me))
#3. It counts each variable seperated by a comma and determined that it was 4.

#Array Exercises
import numpy as np
import matplotlib.pyplot as plt
mixnums = np.array([1,2.0,3,4.0,5,6.0]) 
print(mixnums)
# 1. It turned it into a list of floats without the zero [1. 2. 3. 4. 5. 6.]
mixtypes = np.array( [1,2, 3.0, 4.0,'5','6.0'])
print (mixtypes)
# 2. Turned the array into a list of strings.

Oddarray = np.arange(1,100,2)

logarray = np.logspace(1,5,16)
print (logarray)

plt.plot(logarray)
plt.show
plt.pause(100)




















 
    
       

       