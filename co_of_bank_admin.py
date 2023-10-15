import random
from abc import ABC,abstractmethod
class User(ABC):
    withdraw_histry={}
    diposite_histry={}
    limit=2
   
   
    def __init__(self,name,email,adderess,ac_type) -> None:
        self.name=name
        self.email=email
        self.adderess=adderess
        self.ac_type=ac_type
        self.balance=0
        self. Account_number=random.randint(100,999)

        Admin.Accounts.append(self)
        print(f'\nWelcome {self.name} , your account create successfully')

    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            admin_ins.total_balance+=amount
            self.diposite_histry['Amount']=amount
            print('\nDiposite successful')

    def withdraw(self,amount):
        if amount>self.balance :
            print('\nWithdrawal amount excesed\n')
            return
        
        if admin_ins.is_bankrupt:
            print('\nThe bank is bankrupt\n')
            return
    
        self.balance-=amount
        admin_ins.total_balance-=amount
        self.withdraw_histry['Amount']=amount
        print('\nWithdraw successful')

    def check_balance(self):
        print(self.balance)
    
    def transaction_histry(self):
        for key,value in self.diposite_histry.items():
            print(f'Diposite {key} = {value}\n')
        
        for keys,valus in self.withdraw_histry.items():
            print(f'Withdraw {key} = {valus}\n')
        
    
    def take_loan(self,amount):
        if admin_ins.inactive_loan:
            print('Loan is closed by Admin\n')
            return
        if self.limit<=0:
            print('You exceeded your limit\n')
            return
        
        self.balance+=amount
        admin_ins.total_loan+=amount
        self.limit-=1
        print('\nAmount added successfully to you account')

    def transfer_money(self,ac_num,amount):
        if admin_ins.is_bankrupt:
            print('\nThe bank is bankrupt\n')
            return
        if amount>self.balance:
            print('Insufficiant fund\n')
            return
        if ac_num not in admin_ins.Accounts:
            print('Invalid Account\n')
            return
        else:
            self.balance-=amount
            ac_num.balance+=amount
            print('\nTransaction successful')

    @abstractmethod
    def showInfo(self):
        pass


class Savings(User):
    def __init__(self, name, email, adderess) -> None:
        super().__init__(name, email, adderess, 'savings')

    def showInfo(self):
        print(f'Name of accountent : {self.name}\n')
        print(f'Email : {self.email}\n')
        print(f'Account Number : {self.Account_number}\n')
        print(f'Account Type : {self.ac_type}\n')
        print(f'Balance : {self.balance}\n')

class Current(User):
    def __init__(self, name, email, adderess) -> None:
        super().__init__(name, email, adderess, 'current')

    def showInfo(self):
        print(f'name of accountent : {self.name}\n')
        print(f'Email : {self.email}\n')
        print(f'Account Number : {self.Account_number}\n')
        print(f'Account Type : {self.ac_type}\n')
        print(f'Balance : {self.balance}\n')

        
class Admin:
    Accounts=[]
    def __init__(self,id) -> None:
        self.id=id
        self.total_balance=0
        self.total_loan=0
        self.is_bankrupt=False
        self.inactive_loan=False
    
      

    def create_account(self, name, email, adderess, ac_type):
        self.name=name
        self.email=email
        self.adderess=adderess
        self.ac_type=ac_type
        self.balance=0
        self. Account_number=random.randint(100,999)
        Admin.Accounts.append(self)

    def delete_account(self,account_n):  
        for account in self.Accounts:
            if account.Account_number==account_n:
                self.Accounts.remove(account)

    
    def show_account(self):
        for account in self.Accounts:
            print(f'Name :{account.name}\n')
            print(f'Email :{account.email}\n')
            print(f'Account _num :{account.Account_number}\n')
            print(f'Address :{account.adderess}\n')
            print(f'Account Type :{account.ac_type}\n')
            print(f'Balance :{account.balance}\n')
            
    
    def TotalBalance(self):
        print(self.total_balance)

    def TotalLoan(self):
        print(self.total_loan)

    def on_off_loan(self,status):
        self.active_loan=status
        print('Loan turned off by admin')
        

    def bankrupt(self,is_bankrupt):
        self.is_bankrupt=is_bankrupt
        print('The bank is bankrupt by authority')


admin_ins = Admin('T')  
currentuser = None
while True:
    print('\nWelcome to our Bank\n')
    if currentuser == None:
        ch = input('Login or register as (L/R): ')
        if ch == 'L':
            print('Login as admin or user (A/U)')
            c = input('Enter your choice: ')
            if c == 'A':
                id = input('Enter id, admin: ')
                if id == admin_ins.id:
                    currentuser = admin_ins
                    print('Welcome admin')
                    
                    while True:
                        print('1. Create account')
                        print('2. Delete account')
                        print('3. Show accounts')
                        print('4. Show total balance')
                        print('5. Show total loan')
                        print('6. Turn off loan feature')
                        print('7. Declare bankruptcy')
                        print('8. Logout')
                        print('9. Exit')
                        
                        op = int(input('Enter your option: '))
                        
                        if op == 1:
                            name = input('Enter name: ')
                            email = input('Enter email: ')
                            addr = input('Enter address: ')
                            ac_typ = input('Enter account type: ')
                            currentuser.create_account(name, email, addr, ac_typ)
                            print('Account created successfully\n')

                        elif op == 2:
                            ac_num = int(input('Enter account number: '))
                            currentuser.delete_account(ac_num)

                        elif op == 3:
                            currentuser.show_account()

                        elif op == 4:
                            currentuser.TotalBalance()

                        elif op == 5:
                            currentuser.TotalLoan()

                        elif op == 6:
                            s = input('Enter status: ')
                            currentuser.on_off_loan(s)

                        elif op == 7:
                            s = input('Enter status: ')
                            currentuser.bankrupt(s)

                        elif op == 8:
                            currentuser = None
                            break

                        elif op == 9:
                            exit()

                    currentuser = None
                else:
                    print('Invalid ID')

            elif c == 'U':
                em = input('Enter your email: ')
                for mail in Admin.Accounts:
                    if em == mail.email:
                        currentuser = em
                        break
                else:
                    print('Wrong email')

        elif ch == 'R':
            name=input('Enter name :')
            mail=input('Enter email :')
            addr=input('Enter address :')
            typ=input('Enter account type (SV/CR)')
            if typ=='SV':
                currentuser=Savings(name,mail,addr)
          
            elif typ=='CR':
                currentuser=Current(name,mail,addr)
        else:
            em = input('Enter your email: ')
            for mail in Admin.Accounts:
                if em == mail.email:
                    currentuser = em
                    break
    else:
        print(f'Welcome {currentuser.name}')
        if currentuser.ac_type=='savings':
            print('Savings account user your option given below\n')
            print('1.Deposite')
            print('2.Withdraw')
            print('3.Check balance')
            print('4.Transaction history')
            print('5.Take loan')
            print('6.Transfer amount')
            print('7.Show info')
            print('8.Logout')
            print('9.Exist')

            a=int(input('Enter your option :'))
            if a==1:
                am=int(input('Enter amout :'))
                currentuser.deposite(am)

            elif a==2:
                am=int(input('Enter amount'))
                currentuser.withdraw(am)

            elif a==3:
                print(currentuser.check_balance())

            elif a==4:
                currentuser.transaction_histry()

            elif a==5:
                am=int(input('Enter amount :'))
                currentuser.take_loan(am)
            
            elif a==6:
                am=int(input('Enter amount :'))
                num_ac=int(input('Enter account :'))
                currentuser.transfer_money(num_ac,am)
            
            elif a==7:
                currentuser.showInfo()

            elif a==8:
                currentuser=None

            elif a==9:
                break
        
        else:
            print('Current account user your option given below\n')
            print('1.Deposite')
            print('2.Withdraw')
            print('3.Check balance')
            print('4.Transaction history')
            print('5.Take loan')
            print('6.Transfer amount')
            print('7.Show info')
            print('8.Logout')
            print('9.Exist')

            a=int(input('Enter your option :'))
            if a==1:
                am=int(input('Enter amout :'))
                currentuser.deposite(am)

            elif a==2:
                am=int(input('Enter amount'))
                currentuser.withdraw(am)

            elif a==3:
                currentuser.check_balance()

            elif a==4:
                currentuser.transaction_histry()

            elif a==5:
                am=int(input('Enter amount :'))
                currentuser.take_loan(am)
            
            elif a==6:
                am=int(input('Enter amount :'))
                num_ac=int(input('Enter account :'))
                currentuser.transfer_money(num_ac,am)
            
            elif a==7:
                currentuser.showInfo()

            elif a==8:
                currentuser=None
            elif a==9:
                break
