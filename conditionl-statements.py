'''data = {
    'pransanth@gmail.com': '123@' ,
    'rakeshmodugu79@gmail.com': '1234@',
    'mahi@hmail.com':'5678'


}
email,password = input("Enter your email and password separated by a comma: ").split(',')
if data.get(email) == password:
    print("Login successful")
else:
    print("Login failed, please check your email and password")'''



'''items = ['apple', 'banana', 'cherry']


stocks = [10, 5, 0]
if len(items) == len(stocks):
    print("Items and stocks are in sync.") ''' 



#------------------------------------------------------------------------------------------------------------------------
# Conditional Statements

'''stocks = [20,50,40,0]
distance = [13,4,9,12]
rating =[3.2, 4 4.3,1]
cost = [150, 60,20,40]
veg = [True, False, True, False]
time = [40,30,25,15]
data = input('Enter the Item : ')
ind = items.index(data)
if distance[ind] < 5 and rating[ind] > 4 and cost[ind] < 500 and veg[ind] == True and time[ind] < 30:
    print(" Time, Veg,Cosst,distance and rating applid")
elif distance[ind] < 5 and rating[ind] > 4 and cost[ind] < 500 and veg[ind]:
    print('Time, Veg,Cosst and distance applied')'''


# -----------------------------------------------------------------------------------------------------------------------
# PALINDROME Question
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
'''def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1] 

a = input("Enter a string: ")
if is_palindrome(a):
    print(f"{a} is a palindrome") '''


#------------------------------------------------------------------------------------------------------------------------# FIBONACCI SERIES
'''def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]  
a = int(input("Enter the number of terms in the Fibonacci series: "))
if a <= 0:
    print("Please enter a positive integer.")
else:
    fib_series = fibonacci(a)
    print(f"The first {a} terms of the Fibonacci series are: {fib_series}")  '''
#------------------------------------------------------------------------------------------------------------------------       
# PRIME NUMBER CHECK
''''def is_prime(num):  
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")      
else:
    print(f"{num} is not a prime number.") '''
#------------------------------------------------------------------------------------------------------------------------
# FACTORIAL CALCULATION     

'''def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n = int(input("Enter a non-negative integer to calculate its factorial: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")    '''  
#------------------------------------------------------------------------------------------------------------------------
# ARMSTRONG NUMBER CHECK
'''def is_armstrong(num):
    num_str = str(num)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return sum_of_powers == num
num = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")     
    
else:
    print(f"{num} is not an Armstrong number.")  '''
#------------------------------------------------------------------------------------------------------------------------
# REVERSE A STRING
'''def reverse_string(s):
    return s[::-1]

s = input("Enter a string to reverse: ")
reversed_s = reverse_string(s)  

print(f"The reversed string is: {reversed_s}") '''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A STRING IS A SUBSTRING
'''def is_substring(sub, main):
    return sub in main

sub = input("Enter the substring to check: ")
main = input("Enter the main string: ")


if is_substring(sub, main):
    print(f"'{sub}' is a substring of '{main}'.")   
else:
    print(f"'{sub}' is not a substring of '{main}'.")'''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A STRING IS A PALINDROME
'''def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

s = input("Enter a string to check if it is a palindrome: ")
if is_palindrome(s):
    print(f"'{s}' is a palindrome.")



else:    print(f"'{s}' is not a palindrome.")'''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A NUMBER IS EVEN OR ODD      
'''def is_even(num):
    return num % 2 == 0
num = int(input("Enter a number to check if it is even or odd: "))
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.") '''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A NUMBER IS POSITIVE, NEGATIVE, OR ZERO
'''def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"




num = float(input("Enter a number to check if it is positive, negative, or zero: "))
result = check_number(num)
print(f"The number {num} is {result}.") '''

#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A NUMBER IS PRIME
'''def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.") '''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A NUMBER IS A PERFECT SQUARE
'''import math


def is_perfect_square(num):
    if num < 0:
        return False
    root = int(math.sqrt(num))
    return root * root == num

num = int(input("Enter a number to check if it is a perfect square: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.") '''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A NUMBER IS A FIBONACCI NUMBER

'''def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

num = int(input("Enter a number to check if it is a Fibonacci number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")

else:
    print(f"{num} is not a Fibonacci number.") '''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A NUMBER IS A POWER OF TWO
'''def is_power_of_two(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0

num = int(input("Enter a number to check if it is a power of two: "))
if is_power_of_two(num):
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.") '''
#------------------------------------------------------------------------------------------------------------------------
# CHECK IF A NUMBER IS A PALINDROME NUMBER
'''def is_palindrome_number(num):
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num

num = int(input("Enter a number to check if it is a palindrome number: "))
if is_palindrome_number(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.") '''

#------------------------------------------------------------------------------------------------------------------------

# CHECK IF A NUMBER IS A HARSHAD NUMBER
'''def is_harshad(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

num = int(input("Enter a number to check if it is a Harshad number: "))
if is_harshad(num):


    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.") '''
#--------------------------------------------- ---------------------------------------------------------------------------
# CHECK IF A NUMBER IS A DISARI NUMBER
'''def is_disarium(num):
    num_str = str(num)
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return total == num

num = int(input("Enter a number to check if it is a Disarium number: "))



if is_disarium(num):
    print(f"{num} is a Disarium number.")   
else:
    print(f"{num} is not a Disarium number.") '''
#------------------------------------------------------------------------------------------------------------------------


'''name = {1 : 'pransanth', 2: 'rakesh', 3: 'mahi'}
for i in name.keys():

    
    print(f'{i}, {name[i].capitalize()}') '''

#------------------------------------------------------------------------------------------------------------------------
a = {1:2, 2:3, 3:4, 4:5, 5:6}
for key,value in a.items():
    print(f'{key} : {value}')