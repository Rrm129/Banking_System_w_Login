import random
import time
from datetime import date
from datetime import datetime


class Bankaccount:
    accountNumber = 10000
    accountsDic = {}

    def __init__(self, fname, lname, dob, ssn, password, balance=1000, accNumber=0, transactionHist='0.'):
        if accNumber == 0:
            Bankaccount.accountNumber += random.randint(1, 37)
            self.accountNumber = str(Bankaccount.accountNumber)
        else:
            self.accountNumber = str(accNumber)
        self.lname = lname
        self.fname = fname
        self.dob = str(dob)
        self.ssn = str(ssn)
        self.password = str(password)
        self.balance = balance
        Bankaccount.accountsDic[self.ssn] = self
        self.transactionHist = transactionHist.strip("\n")

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.dob + ' ' + self.ssn + ' ' + self.password + ' ' + str(
            self.balance) + ' ' + self.accountNumber + ' ' + self.transactionHist

    # Getters
    def get_accountNumber(self):
        return self.accountNumber

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_dob(self):
        return self.dob

    def get_ssn(self):
        return self.ssn

    def get_password(self):
        return self.password

    @classmethod
    def get_info_by_ssn(cls, ssn):
        try:
            return cls.accountsDic[ssn]
        except:
            return ""

    def save_in_database(self):
        file = open('accountInfo.txt', 'a+')
        file.write(self.__str__())
        file.write('\n')
        file.close()

    def delete_in_database(self):
        afile = open('accountInfo.txt', 'r')
        lines = afile.readlines()
        afile.close()
        bfile = open('accountInfo.txt', 'w')
        for line in lines:
            if line[0:len(self.fname)] != self.fname:
                bfile.write(line)
        bfile.close()

    def display_info(self):
        print('--------------------- ')
        print('Account:   ', self.accountNumber)
        print('Balance: $ ', self.balance)
        print('---------------------')

    def send_money(self):
        amount = input('Amount To Send: ')
        cc = input('Send to Account: ')
        print('Amount sent!')
        self.balance = int(self.balance) - int(amount)

        today = date.today()
        tdate = str(today.strftime("_%m/%d/%Y"))
        self.transactionHist = self.transactionHist + '-' + amount + tdate + '_S' + '.'

        self.delete_in_database()
        self.save_in_database()
        time.sleep(2.5)

    def deposit_money(self):
        amount = input('Amount To Deposit: ')
        print('$ ', amount, ' deposited!')
        self.balance = int(self.balance) + int(amount)

        today = date.today()
        tdate = str(today.strftime("_%m/%d/%Y"))
        self.transactionHist = self.transactionHist + amount + tdate + '_D' + '.'

        self.delete_in_database()
        self.save_in_database()
        time.sleep(2.5)

    def display_transaction_hist(self):

        if self.transactionHist == '0.':
            print('\nNo Transactions Yet')
            time.sleep(2)
            return
        print('\n')

        transactions = self.transactionHist.split(".")

        for trans in transactions:

            if trans == '0':
                continue
            try:
                amount, date, type = trans.split("_")
            except:
                type = False
                pass

            if type == "D":
                print(date, " - Deposited $", amount)
            elif type == "S":
                print(date, " - Sent $", amount[1:len(amount)])
            else:
                break

        input("\nPress Enter to go back to main menu...")

    def print_information(self):
        print('\nAccount Number: ', self.get_accountNumber())
        print('First Name: ', self.get_fname())
        print('Last Name: ', self.get_lname())
        datestr = self.get_dob()
        dateob = datetime.strptime(datestr, '%m%d%Y').date()
        print('Date of Birth: ', dateob.strftime('%m/%d/%Y'))
        print('Social Security: ', self.get_ssn())

        input("\nPress Enter to go back to main menu...")
