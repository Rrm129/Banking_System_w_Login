from bankclasses import *
import os
import time


def import_users(file):
    ifile = open(file, 'r')
    for line in ifile:
        print(line.rstrip("\n"))
        fname, lname, dob, ssn, password, balance, accNum, transactionHist = line.split(" ")
        account = Bankaccount(fname, lname, dob, ssn, password, balance, accNum, transactionHist)


def open_account():
    ssn = input('Social Security: ')
    fname = input("First Name: ")
    lname = input("Last Name: ")
    dob = input('Date of Birth: ')
    password = input('Password: ')

    myAccount = Bankaccount(fname, lname, dob, ssn, password)
    myAccount.save_in_database()

    print('Account Created!')
    print('Your Account Number is: ', myAccount.get_accountNumber())
    time.sleep(2)


def sign_in() -> object:
    ssn = input('Social Security: ')
    passW = input('Password: ')

    try:
        if Bankaccount.get_info_by_ssn(ssn).get_ssn() == ssn and Bankaccount.accountsDic[ssn].get_password() == passW:
            print('\nLogin Successful')
            print('^^^^^^^^^^^^^^^^')
            time.sleep(2)
            return ssn, False
    except:
        pass

    print("Wrong password or account does not exist")
    time.sleep(1.5)
    return ssn, True


def main():
    x = True
    y = True
    k = True

    while x:

        while y:
            os.system('cls')
            print('\n1) Sign In')
            print('2) Open Account')
            print('3) Close')

            task = input('Input: ')

            if task == '1':
                import_users('accountInfo.txt')
                ssn, y = sign_in()

            if task == '2':
                open_account()

            if task == '3':
                print("Re-run Program")
                x = False
                y = False

        if not x:
            break

        while k:
            os.system('cls')

            Bankaccount.accountsDic[ssn].display_info()

            print('1) Send Money')
            print('2) Deposit')
            print('3) Transaction History')
            print('4) Account Info')
            print('5) Logout')

            task = input('input: ')

            if task == '1':
                Bankaccount.accountsDic[ssn].send_money()

            if task == '2':
                Bankaccount.accountsDic[ssn].deposit_money()

            if task == '3':
                Bankaccount.accountsDic[ssn].display_transaction_hist()

            if task == '4':
                print(Bankaccount.accountsDic[ssn].print_information())

            if task == '5':
                print("Re-run Program")
                x = False
                k = False


if __name__ == '__main__':
    main()
