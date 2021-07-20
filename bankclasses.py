import random


class Bankaccount:
    accountNumber = 10000
    accountsDic = {}

    def __init__(self, fname, lname, dob, ssn, password, balance=1000, accNumber=0):
        if accNumber ==0:
            Bankaccount.accountNumber += random.randint(1, 37)
            self.accountNumber = str(Bankaccount.accountNumber)
        else:
            self.accountNumber = str(accNumber)
        self.lname = lname
        self.fname = fname
        self.dob = str(dob)
        self.ssn = str(ssn)
        self.password = str(password)
        self.balance = str(balance)
        Bankaccount.accountsDic[self.ssn] = self
        self.transactionHistory = []


    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.dob + ' ' + self.ssn + ' ' + self.password + ' ' + str(self.balance) + ' '+ self.accountNumber

    @classmethod
    def get_info_by_ssn(cls, ssn):
        try:
            return cls.accountsDic[ssn]
        except:
            return None

    def save_in_database(self):

        afile = open('ssnNumbers.txt', 'a+')
        afile.seek(0)
        data = afile.read(100)
        if len(data) > 0:
            afile.write('\n')
        afile.write(self.ssn)
        afile.close()

        bfile = open('accountInfo.txt', 'a+')
        bfile.seek(0)
        data = bfile.read(100)
        if len(data) > 0:
            bfile.write('\n')
        bfile.write(self.__str__())
        bfile.close()

    def delete_in_database(self):
        afile = open('accountInfo.txt', 'r')
        lines = afile.readlines()
        bfile = open('accountInfo.txt', 'w')
        for line in lines:
            if line[0:len(self.fname)] != self.fname:
                bfile.write(line)


    def display_info(self):
        print('Account: ', self.accountNumber)
        print('Balance: ', self.balance)

    def send_money(self):
        amount = input('Amount To Send: ')
        cc = input('Account: ')
        self.balance = self.balance - amount
