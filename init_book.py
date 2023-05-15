# The main file for my checkbook app
import os
from os import system
import book_functions as bf


bootup = True
operating = True
while bootup == True:
    os.system('clear')
    bf.greeting()
    bootup = False
while operating == True:
    #os.system('clear')
    bf.account()
    #print("\nPlease select an option: \n1.View Balance \n2.Make deposit \n3.Withdrawal \n4.Exit\n")
    selection = input("Please select an option: 1.View Balance  2.Make deposit  3.Withdrawal  4.Exit\n")
    if selection.isdigit():
        selection = int(selection)
        if selection > 4:
            print('You have entered an invalid response.\nValid responses are #1-4.')
            continue
        elif selection == 1:
            bf.view_balance()
            continue
        elif selection == 2:
            deposit = input('Enter the amount to deposit:')
            #deposit = bf.data_scrub(deposit)
            #deposit = float(deposit)
            if bf.isfloat(deposit) == False:
                print('You have entered an invalid response.\nValid responses are DFP.')
                continue
            else:
                bf.deposit_funds(deposit)
                continue
        elif selection == 3:
            wdf = input('Enter the amount to withdrawal:')
            if bf.isfloat(wdf) == False:
                print('You have entered an invalid response.\nValid responses are DFP.')
            else:
                bf.with_funds(wdf)
                continue
        else:
            bf.parting()
            break
    else:
        print('You have entered an invalid response.')
        continue
