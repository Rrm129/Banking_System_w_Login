from bankclasses import *
import os
import time

def read_file(file):
    ifile = open(file, 'r')
    for line in ifile:
        print(line)
    ifile.close()

def import_users(file):
    ifile = open(file, 'r')
    for line in ifile:
        print(line.rstrip("\n"))
        fname, lname, dob, ssn, password, balance, accNum = line.split(" ")
        account = Bankaccount(fname, lname, dob, ssn , password, balance, accNum)

def open_account():
    ssn = input('Social Security: ')
    fname = input("First Name: ")
    lname = input("Last Name: ")
    dob = input('Date of Birth: ')
    password = input('Password: ')

    myAccount = Bankaccount(fname, lname, dob, ssn, password)
    myAccount.save_in_database()

    print('Account Created!')
    print('Your Account Number is: ', myAccount.accountNumber)
    time.sleep(2)


def sign_in():
    ssn = input('Social Security: ')
    passW = input('Password: ')
    try:
        if Bankaccount.get_info_by_ssn(ssn).ssn == ssn and Bankaccount.accountsDic[ssn].password == passW:
            print('\nLogin Successful')
            print('^^^^^^^^^^^^^^^^')
            time.sleep(2)
            return ssn, False
    except:
        print("Wrong password or account does not exist")
        time.sleep(1)
        return None, True

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
            print('1) Display Balance')
            print('2) Deposit')
            print('3) Withdraw')
            print('4) Loan')
            print('5) Logout')

            task = input('input: ')

            if task == '1':
                print('Account Number: ', Bankaccount.accountsDic[ssn].accountNumber)
                print('Available Balance: $', Bankaccount.accountsDic[ssn].balance)
                time.sleep(3)

            if task == '2':
                Bankaccount.accountsDic[ssn].send_money()


            if task == '5':
                print("Re-run Program")
                Bankaccount.accountsDic[ssn].delete_in_database()
                Bankaccount.accountsDic[ssn].save_in_database()
                x = False
                k = False


if __name__ == '__main__':
    main()
