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


class A :
    def __init__(self,v1,v2): # self = instance
        self.var1 = v1  
        self.var2 = v2  
        print("init method") 

obj=A(10,20) # obj creation  1
vamsi=A("vamsi","ravi") # obj creation 2 
ravi=A([1,2,3],{"id":1,"name":"vamsi"}) # obj creation 3