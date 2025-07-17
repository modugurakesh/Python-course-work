data = {
    123:{'pin':123,'current_balance':4000,'history':[]},
    456:{'pin':123,'current_balance':5000,'history':[]},
    111:{'pin':123,'current_balance':7000,'history':[]},
    }
print('Welcome to th ATM')
print(data[123])
account_number = int(input('Enter your account number: '))
pin = int(input('Enter your pin: '))

''''if account_number in data and data[account_number]['pin'] == pin:
    print('Login successful')
    while True:
        print('ATM Menu:')
        print('1. Check balance')
        print('2. Deposit money')
        print('3. Withdraw money')
        print('4. Exit')
        print('5. history:', data[account_number]['history'])
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print(f'Your current balance is: {data[account_number]["current_balance"]}')
        elif choice == 2:
            amount = float(input('Enter the amount to deposit: '))
            data[account_number]['current_balance'] += amount
            data[account_number]['history'].append(f'Deposited: {amount}')
            print(f'You have successfully deposited {amount}. New balance is {data[account_number]["current_balance"]}')    
        elif choice == 3:

            amount = float(input('Enter the amount to withdraw: '))
            if amount > data[account_number]['current_balance']:
                print('Insufficient balance')
            else:
                data[account_number]['current_balance'] -= amount
                data[account_number]['history'].append(f'Withdrew: {amount}')
                print(f'You have successfully withdrawn {amount}. New balance is {data[account_number]["current_balance"]}')
        elif choice == 4:
            print('Thank you for using the ATM. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')
else:
    print('Invalid account number or pin. Please try again.') '''
#