# # single - level inheritance 
# # the inheritance involves with one parent and one child 


# class Parent:
#     name="srinu" 
#     surName="Enduri"
    
#     def __init__(self):
#         print("parent init method")

#     def properties(self):
#         gold=1
#         land=1
#         print(gold,land)    

# class Child(Parent):
#     name="vamsi"
#     # print(super().name)
#     def __init__(self,age,height):
#         self.a=age
#         self.h=height
#         print("child init method") 
#         print(super().surName)
#         print(super().surName)
#         print(super().name)
#         super().properties()

#     def mynamewithsurname(self,num):
#         self.n =num  #instance var
#         n=num # local var
#         print(Child.name,super().surName)    

# obj=Child(27,5.5)
# obj.mynamewithsurname(100)






# multi-level inheritance
abc="Status"
class Parent:
    name="GVR"
    def __init__(self,v1,v2):
        print("parent init method")
        print(abc)
        print(v1,v2)
class Child(Parent):
    name="Gude"
    def __init__(self,v1,v2):
        print(v1,v2)
        print("child init method")
        print(super().name)
        super().__init__(v1,v2)

class grandChild(Child):
    name="Nani"
    def __init__(self,v1,v2):
        print("g_child init method")
        print(super().name)
        super().__init__(v1,v2)
    
obj=grandChild(input("enter value 1"),input("enter value 2"))    






# what is oops ?
# what are features of oops ?
# what is class ?
# what is obj ?
# what is self ?
# what is __init__() ?
# what are pilars of oops ?
# what is iheritance ? types of inheritance ?
# what is single levl inheritance and give one code example ?
# what is multi level inheritance and give one code example ?