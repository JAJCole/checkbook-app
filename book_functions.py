# This file contains functions to be used in my checkbook app.
import os

# Create account file on startup. -- changes to add: multiple users
user_data = 'user_data.txt'


def account():
    if os.path.exists(user_data) == False:
        with open(user_data, 'w') as f:
            f.write('0.00')
    else:
        pass


# Transform inputs and data into numeric form if needed
def data_scrub(data):
    return float(data.replace(',',''))


# View Balance
def view_balance():
    if os.path.exists(user_data) == True:
        with open(user_data,'r') as f:
            last_data = f.readlines()[-1]
            return print('BALANCE:  ${:0.2f}'.format(float(last_data)))


# Deposit Funds    
def deposit_funds(deposit):
    if os.path.exists(user_data) == True:
        with open(user_data,'r') as f:
            last_data = f.readlines()[-1]
            last_data = data_scrub(last_data)
            deposit = data_scrub(deposit)
            new_bal_ = last_data + deposit
        with open(user_data,'a') as f:
            f.writelines('\n{}'.format(new_bal_))


# Withdrawal funds
def with_funds(wdf):
    if os.path.exists(user_data) == True:
        with open(user_data,'r') as f:
            last_data = f.readlines()[-1]
            last_data = data_scrub(last_data)
            wdf = data_scrub(wdf)
            new_bal = last_data - wdf
        with open(user_data,'a') as f:
            f.writelines('\n{}'.format(new_bal))

# Welcome message
def greeting():
    message = 'Welcome to Checkbook App'
    return print(message)


# Parting message
def parting():
    bye_mess = 'Thank you for using Checkbook App. Have a nice day.'
    return print(bye_mess)



def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False