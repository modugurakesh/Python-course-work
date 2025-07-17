# 1. Arithmetic Operators


'''a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Addition:", a + b )   
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("  ")
print("--------------------------------------------------------------------------------------------------")
print("  ") '''

#---------------------------------------------------------------------------------------------------------

# 2. Comparison Operators

'''a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Is a equal to b?", a == b)  
print("Is a not equal to b?", a != b)
print("Is a greater than b?", a > b)
print("Is a less than b?", a < b)
print("Is a greater than or equal to b?", a >= b)
print("Is a less than or equal to b?", a <= b)  
print("  ")
print("--------------------------------------------------------------------------------------------------")
print("  ") '''

#----------------------------------------------------------------------------------------------------------

# 3. Assignment Operators


'''a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
a += b 
print('a += b : ',a)
a -= b 
print('b -= b : ', a)
print(' ')

frist_number = int(input('Enter a input: '))
second_number = int(input('Enter a number : '))

 
frist_number /= second_number 
print('frist_number *= second_number: ', frist_number)
print('frist_number /= second_number : ', )

print() '''


#---------------------------------------------------------------------------------------------------------------

#  4. Logical Operators (Using Logic Gates)

'''a = int(input("Enter a number: "))
b = int(input('Enter a second Input: '))
print("Logical AND:", a and b)
print("Logical OR:", a or b)
print('a != b : ', a != b)
print('a % 2 == 0 and a % 10 ==0 : ',a % 2 == 0 and a % 10 ==0) '''


#---------------------------------------------------------------------------------------------------------------

# 5. Membership Operators

'''my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True 
print(6 not in my_list)  # True
print(' ')
my_string = "Hello, World!"
print("Hello" in my_string)  # True
print("Python" not in my_string)  # True
print(' ')

my_tuple = (1, 2, 3)
print(2 in my_tuple)  # True
print(4 not in my_tuple)  # True
my_set = {1, 2, 3}
print(1 in my_set)  # True
print(' ')

print(4 not in my_set)  # True
my_dict = {'a': 1, 'b': 2}
print('a' in my_dict)  # True (checks keys)
print(1 in my_dict.values())  # True (checks values)
print('c' not in my_dict)  # True (checks keys)  '''


#---------------------------------------------------------------------------------------------------------------
# 6. Identity Operators

'''a = [1, 2, 3]
b = a   
print(a is b)  # True (same object)
print(a is not b)  # False (same object)
c = a.copy()
prin(c)  # [1, 2, 3] (same content)
print(a is c)  # False (different object)
print(a is not c)  # True (different object)

d = [1, 2, 3]
print(a == d)  # True (same content)
print(a is d)  # False (different object)
print(a is not d)  # True (different object)
'''
#---------------------------------------------------------------------------------------------------------------

# 7. Bitwise Operators



'''a = 5  # 0101 in binary
b = 3  # 0011 in binary
print("Bitwise AND:", a & b)  # 0001 in binary (1 in decimal)
print("Bitwise OR:", a | b)  # 0111 in binary (7 in decimal)
print("Bitwise XOR:", a ^ b)  # 0110 in binary (6 in decimal)
print("Bitwise NOT:", ~a)  # Inverts bits (in Python, it gives -6 for 5)
print("Left Shift:", a << 1)  # 1010 in binary (10 in decimal)
print("Right Shift:", a >> 1)  # 0010 in binary (2 in decimal)'''

'''a = 6 # 0110 in binary
b = 3 # 0011 in binary
print("Bitwise AND:", a & b)  # 0010 in binary (2 in decimal)
print("Bitwise OR:", a | b)   # 0111 in binary (7 in decimal)
print("Bitwise XOR:", a ^ b)  # 0101 in binary (5 in decimal)
print("Bitwise NOT:", ~a)  # Inverts bits (in Python, it gives -7 for 6) '''

#---------------------------------------------------------------------------------------------------------------    
# 8. Ternary Operator

'''a = 10
b = 20

max_value = a if a > b else b
print("Maximum value is:", max_value)  # Output: Maximum value is: 20 '''

#---------------------------------------------------------------------------------------------------------------
# 9. Operator Precedence

'''a = 10
b = 5
c = 2
result = a + b * c - a / b ** c
print("Result of expression:", result)  # Output: Result of expression: 10.0 ''' 
#---------------------------------------------------------------------------------------------------------------
# 10. Chaining Comparison Operators

'''
x = 5
y = 10
z = 15
print(x < y < z)  # True (5 < 10 < 15)

print(x < y > z)  # False (5 < 10 is True, but 10 > 15 is False)

print(x < y == z)  # False (5 < 10 is True, but 10 == 15 is False)
print(x < y < z > x)  # True (5 < 10 < 15 > 5)


print(x < y < z < 20)  # True (5 < 10 < 15 < 20)
print(x < y < z < 10)  # False (5 < 10 < 15 < 10 is False)
print(x < y < z < 15)  # False (5 < 10 < 15 < 15 is False)

print(x < y < z < 30)  # True (5 < 10 < 15 < 30)
print(x < y < z < 25)  # True (5 < 10 < 15 < 25)
print(x < y < z < 20)  # True (5 < 10 <15 < 20)
print(x < y < z < 15)  # False (5 < 10 <            '''