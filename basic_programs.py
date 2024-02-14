# Factorial 
'''
# python program to check if x is a perfect square
import math

# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x

# Returns true if n is a Fibonacci Number, else false
def isFibonacci(n):

	# n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
	# is a perfect square
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
	
# A utility function to test above functions
for i in range(1,11):
	if (isFibonacci(i) == True):
		print i,"is a Fibonacci Number"
	else:
		print i,"is a not Fibonacci Number "

---------------------
def is_palindrome(s):
    res = []
    s = ['']
    if len(s) < 2:
        return True
    else:
        rev_s = is_palindrome(s[1:]) + s[0]
        res.append(rev_s)
        if res == s:
            return True
        return False
----------------------------

# Python 3 program to find 
# factorial of given number
def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact *= n
			n -= 1
		return fact

# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))

# This code is contributed by Dharmik Thakkar

----------------------
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))



def factorial(n):
       
    res = 1
      
    for i in range(2, n+1):
        res *= i
    return res
 # Driver Code
num = 5
print("Factorial of", num, "is",
factorial(num))


-------------------------------------------

# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320

print_factors(num)

------------------------------------------

# Display the powers of 2 using anonymous function

terms = 10

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])

-------------------------------------------
SImple interest
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si


# Python3 program to find compound
# interest for given values.


def compound_interest(principal, rate, time):

	# Calculates compound interest
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount - principal
	print("Compound interest is", CI)


# Driver Code
compound_interest(10000, 10.25, 5)



Armstrong number
def is_armstrong(num):
	num_str = str(num)
	n = len(num_str)
	sum = 0
	for digit in num_str:
		sum += int(digit)**n
	if sum == num:
		return True
	else:
		return False
num=153
print(is_armstrong(num))

----------------------------------

# python 3 program
# to check whether the given number is armstrong or not
# without using power function

n = 153 # or n=int(input()) -> taking input from user
s = n # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
	r = n % 10
	sum1 = sum1+(r**b)
	n = n//10
if s == sum1:
	print("The given number", s, "is armstrong number")
else:
	print("The given number", s, "is not armstrong number")

# This code is contributed by Gangarajula Laxmi


-----------------------------------------------------

Python Program to Print all Prime numbers in an Interval
# Python program to print all
# prime number in an interval

def prime(x, y):
	prime_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return prime_list

# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
	print("There are no prime numbers in this range")
else:
	print("The prime numbers in this range are: ", lst)

    ---------------------------------------------


    # Python program to print all
# prime number in an interval

def prime(starting_range, ending_range):
lst=[]
flag=0				 #Declaring flag variable
for i in range(starting_range, ending_range):#elements range between starting and ending range 
	for j in range(2,i): 
	if(i%j==0):	 #checking if number is divisible or not
		flag=1	 #if number is divisible, then flag variable will become 1
		break
	else:
		flag=0	
	if(flag==0): #if flag variable is 0, then element will append in list 
	lst.append(i)
return lst

# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
	print("There are no prime numbers in this range")
else:
	print("The prime numbers in this range are: ", lst)

    -------------------------------------
if num is a prime number or not

num = 11
# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):
		
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")

-----------------------------------

    Python Program to Check Prime Number
    num = 11
# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")

    
-------------------------------------------
    Fibonacci series


# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program

print(fibonacci(9))

--------------------------------------

using recursion

# Function for nth Fibonacci number

def Fibonacci(n):
	if n<= 0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n == 1:
		return 0
	# Second Fibonacci number is 1
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(10))


Python Program for How to check if a given number is Fibonacci number?
# python program to check if x is a perfect square
import math

# A utility function that returns true if x is perfect square


def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x

# Returns true if n is a Fibonacci Number, else false


def isFibonacci(n):

	# n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
	# is a perfect square
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


# A utility function to test above functions
for i in range(1, 11):
	if (isFibonacci(i) == True):
		print(i, "is a Fibonacci Number")
	else:
		print(i, "is a not Fibonacci Number ")

        


        Python Program for nth multiple of a number in Fibonacci Series
        # Python Program to find position of n\'th multiple
# of a number k in Fibonacci Series

def findPosition(k, n):
	f1 = 0
	f2 = 1
	i =2; 
	while i!=0:
		f3 = f1 + f2;
		f1 = f2;
		f2 = f3;

		if f2%k == 0:
			return n*i

		i+=1
		
	return


# Multiple no.
n = 5;
# Number of whose multiple we are finding
k = 4;

print("Position of n\'th multiple of k in"
				"Fibonacci Series is", findPosition(k,n));

# Code contributed by Mohit Gupta_OMG

--------------------------------------------------

Program to print ASCII Value of a character
# Python program to print 
# ASCII Value of Character 

# In c we can assign different 
# characters of which we want ASCII value 

c = 'g'
# print the ASCII value of assigned character in c 
print("The ASCII value of '" + c + "' is", ord(c)) 


Python Program for Sum of squares of first n natural numbers
# Python3 Program to
# find sum of square
# of first n natural
# numbers


# Return the sum of
# square of first n
# natural numbers

def squaresum(n):

	# Iterate i from 1
	# and n finding
	# square of i and
	# add to sum.
	sm = 0
	for i in range(1, n+1):
		sm = sm + (i * i)

	return sm


# Driven Program
n = 4
print(squaresum(n))

# This code is contributed by Nikita Tiwari.*/




Python Program for cube sum of first n natural numbers
# Simple Python program to find sum of series
# with cubes of first n natural numbers

# Returns the sum of series 
def sumOfSeries(n):
	sum = 0
	for i in range(1, n + 1):
		sum += i * i*i
		
	return sum


# Driver Function
n = 5
print(sumOfSeries(n))

# Code Contributed by Mohit Gupta_OMG <(0_o)>




Python Program to Find Largest Element in an Array
# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


def largest(arr, n):

	# Initialize maximum element
	max = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)
-----------------------------------------

# Python code to demonstrate naive
# method to compute gcd or hcf( Loops )

def computeGCD(x, y):

	if x > y:
		small = y
	else:
		small = x
	for i in range(1, small + 1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i
			
	return gcd

a = 60
b = 48

# prints 12
print ("The gcd of 60 and 48 is : ", end="")
print (computeGCD(60,48))
-----------------------------------------------

import random
rand_num = random.random()
rand1 = random.randint(0,9)
print(rand_num)
print(rand1)
----------------

# Leap year
year = 2000

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
-------------------------------------------------

n1 = 20
n2 = 30
n3 = 90
if n1>n2 and n2>n3:
    print("n1 is greater")
elif n2>n1 and n2>n3:
    print("n2 is greater")
else:
    print("n3 is greater")
------------------------------------

# match random number and entered number

import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
--------------------------------------

# How to Build a Password Checker in Python

def password_checker(password):
    # Define the criteria for a strong password
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"
    
    # Check the length of the password
    if len(password) < min_length:
        print("Password is too short!")
        return False
    
    # Check if the password contains an uppercase letter, lowercase letter, digit, and special character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True
    
    # Print an error message for each missing criteria
    if not has_uppercase:
        print("Password must contain at least one uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain at least one lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain at least one digit!")
        return False
    if not has_special_char:
        print("Password must contain at least one special character!")
        return False
    
    # If all criteria are met, print a success message
    print("Password is strong!")
    return True

# Prompt the user to enter a password and check if it meets the criteria
password = input("Enter a password: ")
password_checker(password)
------------------------------------------------------------------------

# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
---------------------------------------------
# Program to find the ASCII value of the given character

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
# ----------------------------------------------------

# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))
-----------------------------------------------

# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
-----------------------------------

# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2014  # year
mm = 11    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
-------------------------------
# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
----------------------------------
# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
--------------------------------------------------------------

# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
----------------------

# punctuations = !()-[]{};:'"\,<>./?@#$%^&*_~

# my_str = "Hello!!!, he said ---and went."

# # To take input from the user
# # my_str = input("Enter a string: ")

# # remove punctuation from the string
# no_punct = ""
# for char in my_str:
#    if char not in punctuations:
#        no_punct = no_punct + char

# # display the unpunctuated string
# print(no_punct)
------------------------

# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
---------------------------------

# patterns

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
-----------------------

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")
-----------------------------
A
B B
C C C
D D D D
E E E E E
Source Code
rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")
----------------------
* * * * *
* * * *
* * *
* *
*
Source Code
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print("\n")
-----------------------
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
Source Code
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()
---------------------------
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5
Source Code
rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()
-----------------------------
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
Source Code
rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()
    --------------
1
2 3
4 5 6
7 8 9 10
Source Code
rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()
-------------------------
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1
Source Code
rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()
-------------------------

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
dict_1.update(dict_2)
print(dict_1)
--------------------------
# Python Program to Access Index of a List Using for Loop
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)
------------------------------------
Sort the dictionary based on values
dt = {5:4, 1:6, 6:3}

sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}

print(sorted_dt)
-----------------------
dt = {5:4, 1:6, 6:3}

sorted_dt_value = sorted(dt.values())
print(sorted_dt_value)
Run Code
Output

[3, 4, 6]
----------------------------
my_list = []
if not my_list:
    print("the list is empty")
--------------------------------
check if key is present in the dict
my_dict = {1: 'a', 2: 'b', 3: 'c'}

if 2 in my_dict:
    print("present")
-------------------------
# Python Program to Split a List Into Evenly Sized Chunks
def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))
---------------------------------------

Python Program to Convert String to Datetime

from datetime import datetime

my_date_string = "Mar 11 2011 11:31AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)
------------------------------------

Python Program Read a File Line by Line Into a List

with open("data_file.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)
------------------------------

# Python Program to Count the Occurrence of an Item in a List
freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(freq)
-----------------------------------

Python Program to Find All File with .txt Extension Present Inside a Directory

import glob, os

os.chdir("my_dir")

for file in glob.glob("*.txt"):
    print(file)
----------------------------------

Python Program to Get the Full Path of the Current Working Directory

import pathlib

# path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())
-------------------------------------

Python Program to Iterate Through Two Lists in Parallel

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

for i, j in zip(list_1, list_2):
    print(i, j)
---------------------------------------

Python Program to Check the File Size

import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)
------------------------------------
Python Program to Count the Number of Digits Present In a Number
num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))
-----------------------------------------------
Python program to check if two strings are anagrams using sorted()
str1 = "Race"
str2 = "Care"

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")
--------------------------------------------------------
Python Program to Capitalize the First Character of a String

my_string = "programiz is Lit"

print(my_string[0].upper() + my_string[1:])
------------------------------------------------

Python Program to Count the Number of Occurrence of a Character in String

count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
----------------------------------

Python Program to Remove Duplicate Element From a List

list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))
------------------------------------

# Python program to split array and move first
# part to end.


def splitArr(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]

		arr[n-1] = x


# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
	print(arr[i], end=' ')
-----------------------------
# This code finds the remainder of the product of all the elements in the array arr divided by 'n'.
def findremainder(arr, len, n):
	product = 1
	for i in range(len):
		product = product * arr[i]
	return product % n


arr = [100, 10, 5, 25, 35, 14]
len = len(arr)
n = 11
print(findremainder(arr, len, n))
--------------------------------------
Python program to solve quadratic equation

import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   
------------------------------------------------------

import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  
print(calendar.month(yy,mm))  
--------------------------------

# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
-------------------------------------------------

# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))

---------------------------------------------

# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

---------------------------------------------------------------

# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)
print()

-----------------------

# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
-----------------------

# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

-------------------

# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
----------------------------
# merge dictionaries

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)
----------------------
# Python Program to Get a Substring of a String

my_string = "I love python."

# prints "love"
print(my_string[2:6])

# prints "love python."
print(my_string[2:])

# prints "I love python"
print(my_string[:-1])
------------------------
# Python Program to Randomly Select an Element From the List
import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))
----------------------------------
# Python Program to Check If a String Is a Number (Float)
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('s12'))
print(isfloat('1.123'))
----------------------------
# Python Program to Append to a File

with open("my_file.txt", "a") as f:
   f.write("new text")
------------------------------------
# Python Program to Delete an Element From a Dictionary
my_dict = {31: 'a', 21: 'b', 14: 'c'}

del my_dict[31]

print(my_dict)
------------------------------------
# Python Program to Convert Two Lists Into a Dictionary

index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = dict(zip(index, languages))
print(dictionary)
-------------------------------

# Python Program to Get Line Count of a File

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len("my_file.txt"))
----------------------------------
# Python Program to Get the Full Path of the Current Working Directory
import pathlib

# path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())
------------------------------------
# Python Program to Count the Number of Digits Present In a Number

num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))
------------------------------------------

Calculate power of a number using a while loop
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))
-----------------------------------

Python program to check if two strings are anagrams using sorted()
str1 = "Race"
str2 = "Care"

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")
---------------------------------------------------------

# Program to Capitalize the First Character of a String

my_string = "programiz is Lit"

print(my_string[0].upper() + my_string[1:])

or------------------------

my_string = "programiz is Lit"

cap_string = my_string.capitalize()

print(cap_string)
-------------------------------------------
# Python Program to Count the Number of Occurrence of a Character in String

count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
---------------------------

# Python Program to Remove Duplicate Element From a List

list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))

-------------------------

# Python Program for Find sum of odd factors of a number

# Formula based Python3 program 
# to find sum of all divisors 
# of n. 
import math 
# Returns sum of all factors 
# of n. 
def sumofoddFactors( n ): 
	
# Traversing through all 
# prime factors. 
res = 1
	
# ignore even factors by 
# of 2 
while n % 2 == 0: 
	n = n // 2
	
for i in range(3, int(math.sqrt(n) + 1)): 
		
	# While i divides n, print 
	# i and divide n 
	count = 0
	curr_sum = 1
	curr_term = 1
	while n % i == 0: 
		count+=1
			
		n = n // i 
		curr_term *= i 
		curr_sum += curr_term 
		
	res *= curr_sum 
	
# This condition is to 
# handle the case when 
# n is a prime number. 
if n >= 2: 
	res *= (1 + n) 
	
return res 

# Driver code 
n = 30
print(sumofoddFactors(n)) 

# This code is contributed by “Sharad_Bhardwaj”.
---------------------------------------------------

name = "Ram"
age = 22
message = "My name is {0} and I am {1} years \
					old. {1} is my favorite \
					number.".format(name, age)
print(message)


or-

# using format option in a simple string
print("{}, A computer science portal for geeks."
	.format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))
---------------------------------------------

# Program to Print Palindrome Numbers in a Range in Python

# Give the lower limit range as static input and store it in a variable.
gvn_lowrlmt = 50
# Give the upper limit range as static input and store it in another variable.
gvn_upprlmt = 130
print("The palindrome numbers between",
      gvn_lowrlmt, "and", gvn_upprlmt, "are:")
# Loop from lower limit range to upper limit range using For loop.
for m in range(gvn_lowrlmt, gvn_upprlmt+1):
    # Inside the loop, give the iterator value as the number of the for loop.
    given_num = m
    # taking another variable to store the copy of original number
    # and initialize it with given num
    duplicate_num = given_num
    # Take a variable reverse_number and initialize it to null
    reverse_number = 0
    # using while loop to reverse the given number
    while (given_num > 0):
        # implementing the algorithm
        # getting the last digit
        remainder = given_num % 10
        reverse_number = (reverse_number * 10) + remainder
        given_num = given_num // 10
   # if duplicate_num and reverse_number are equal then it is palindrome
    if(duplicate_num == reverse_number):
        # Print "duplicate_num "to get the above palindrome number.
        print(duplicate_num, end=" ")
-----------------------------------
# rev str without slicing

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

--------------------

# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
-----------------

# Python 3 program to find 
# factorial of given number
def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact *= n
			n -= 1
		return fact

# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))

# This code is contributed by Dharmik Thakkar
-----------------------------------------------

# Function for nth fibonacci number 
def fibonacci(n):
	a = 0
	b = 1
	
	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")
		
	# Check is n is equal
	# to 0
	elif n == 0:
		return 0
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program
print(fibonacci(9))
----------------------

# Python code to demonstrate naive method
# to compute factorial
n = 23
fact = 1

for i in range(1, n+1):
	fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)
--------------------------------------

Python Program to Find the Fibonacci Series without Using Recursion

first_num = int(input("Enter the first number of the fibonacci series... "))
second_num = int(input("Enter the second number of the fibonacci series... "))
num_of_terms = int(input("Enter the number of terms... "))
print(first_num,second_num)
print("The numbers in fibonacci series are : ")
while(num_of_terms-2):
   third_num = first_num + second_num
   first_num=second_num
   second_num=third_num
   print(third_num)
   num_of_terms=num_of_terms-1
------------------------------------------
Python Program to find the factorial of a number without recursion

my_num = int(input("Enter a number :"))
my_factorial = 1
while(my_num>0):
   my_factorial = my_factorial*my_num
   my_num=my_num-1
print("The factorial of the number is : ")
print(my_factorial)
--------------------------

def is_palindrome(s):
    res = []
    s = ['']
    if len(s) < 2:
        return True
    else:
        rev_s = is_palindrome(s[1:]) + s[0]
        res.append(rev_s)
        if res == s:
            return True
        return False
------------------------------
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
------------------------------------------------

'''