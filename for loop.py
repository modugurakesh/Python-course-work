'''a = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")  '''
# ----------------------------------------------------------------------------------------------------------
# triangle pattern
'''a = int(input("Enter a number: "))
for i in range(1, a + 1):   
    for j in range(1, i + 1):
        print("*", end="")
    print()  # Move to the next line after each row '''

# ----------------------------------------------------------------------------------------------------------

# butterfly pattern
'''a = int(input('Enter a number  : ' ))
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # Move to the next line after each row
for i in range(a - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # Move to the next line after each row ''' 
# ----------------------------------------------------------------------------------------------------------
'''email,pwd = 'xyz@gmail.com', 'xyaz123'
max_attempts = 5 
cur_attempts = 0 
while cur_attempts <= max_attempts:
    email_input = input("Enter your email: ")
    pwd_input = input("Enter your password: ")
    
    if email_input == email and pwd_input == pwd:
        print("Login successful!")
        break
    else:
        cur_attempts += 1
        print(f"Incorrect credentials. You have {max_attempts - cur_attempts} attempts left.")
    cur_attempts += 1
else:   
    print("Maximum attempts reached. Please try again later.") '''
# ----------------------------------------------------------------------------------------------------------  


data = {
    1 : {'name':'rakesh', 'exam-result': True,'python' :100 ,'sql' : 90,'html' : 80},
    2 : {'name':'suresh', 'exam-result': True,'python ':90 ,'sql' : 80,'html' : 70},
    3 : {'name':'mahesh', 'exam-result': True,'python': 80 ,'sql' : 70,'html' : 60},
    4 : {'name':'suresh', 'exam-result': True,'python': 70 ,'sql' : 60,'html' : 50}
}
for i in data.keys():
    print(f"Student ID: {data[i]['name']}")