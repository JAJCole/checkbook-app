import os
user_data = 'user_data.txt'


# Terminal Selection
#def options():
#    selection = ("Please select an option/n1.View Balance/n2.Make deposit/n3.Withdrawal/n4.Exit")
#    return selection


# Withdrawal Attempt
#def with_funds(wdf):
#    if os.path.exists(user_data) == True:
#        with open(user_data,'a') as f:
#            subtr_balance = f.writelines(wdf)

# Withdrawal funds
def with_funds(wdf):
    if os.path.exists(user_data) == True:
        with open(user_data,'r') as f:
            last_data = f.readlines()[-1]
            last_data = data_scrub(last_data)
            wdf = data_scrub(wdf)
            new_bal = last_data + wdf
        with open(user_data,'a') as f:
            f.writelines(new_bal)


# Deposit Attempt
#def deposit_funds(deposit):
#    if os.path.exists(user_data) == True:
#        with open(user_data,'a') as f:
#            update_balance = f.writelines(deposit)

# Deposit funds
def deposit_funds(deposit):
    if os.path.exists(user_data) == True:
        with open(user_data,'r') as f:
            last_data = f.readlines()[-1]
            last_data = data_scrub(last_data)
            deposit = data_scrub(deposit)
            new_bal_ = last_data + deposit
        with open(user_data,'a') as f:
            f.writelines(new_bal_)


# View Attempt
#def view_balance():
#    if os.path.exists(user_data) == True:
#        with open(user_data,'r') as f:
#            balance = f.readlines()
#            return balance

# View Balance
def view_balance():
    if os.path.exists(user_data) == True:
        with open(user_data,'r') as f:
            last_data = f.readlines()[-1]
            return last_data


# Transform inputs and data into numeric form if needed
def data_scrub(data):
    return float(data.replace(',',''))

