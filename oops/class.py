# # class is a col of variables and methods 
# # class is blue-print of obj
# # attributes + methods = properties of class



# # class 
# # cls variables
# # methods 

# # method - method variables -- function var r local var 
# # class memeory allocaton direct line read chestunnapudu automatic 

# name="vamsi"
# def loc():
#     print("hyd kphb phase 1 rod no 4 near remedy hospitals")
# loc()

# class A:
#     # variables / attributes
#     x=10 # class var
#     y=20 # class var
#     z=30 # class var
#     print(x+y+z)

#     #functions / methods
#     def personal_details():
#         m=10 #function var r local var 
#         n=20 #function var r local var
#         print("p details function which is created by developer")
#     personal_details()    

#     def job_details():
#         print("j details function which is created by developer")    
#     job_details()  

# __*abc__()
# __abc()
# _abc()
# b()
# a()
# __init__() :-- function pre-defined user-default



#  class A:
#     # one __init method only in a certain class
#     # no need to call the __init__ method
#     def __init__():
#         print("init method")

#     # variables / attributes
#     x=10 # class var
#     y=20 # class var
#     z=30 # class var
#     print(x+y+z)

#     #functions / methods
#     def personal_details():
#         m=10 #function var r local var 
#         n=20 #function var r local var
#         print("p details function which is created by developer")
#     # personal_details()    

#     def job_details():
#         print("j details function which is created by developer")    
#     # job_details() 



# obj :-- it is real entity and instance of a class
# self :-- instance of A / instance of class 
# class A :
#     pass 
# obj=A() # obj creation 
# print(obj)   



# def __init__(self):
#     return self 
# obj=self   
# print(obj) # self :-- instance of class


# class A :
#     def __init__(self,v1,v2): # self = instance
#         self.var1 = v1  
#         self.var2 = v2  
#         print("init method") 

# obj=A(10,20) # obj creation  1
# vamsi=A("vamsi","ravi") # obj creation 2 
# ravi=A([1,2,3],{"id":1,"name":"vamsi"}) # obj creation 3










class BankAccount:
    bank_name = "State Bank Of India"

    def __init__(self, acc_holder, acc_number, bal):

        self.account_holder = acc_holder
        self.account_number = acc_number
        self.balance = bal
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_details(self):
        
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Bank:", BankAccount.bank_name)
        print("----------------------")


account1 = BankAccount("Hemanth", 1001, 10000)
account2 = BankAccount("Venu Gopal", 1002, 20000)




account1.deposit(5000)
account1.withdraw(2000)       # Calling Methods
account1.display_details()

account2.deposit(3000)
account2.withdraw(5000)         # Calling Methods
account2.display_details()