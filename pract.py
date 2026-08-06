# print(True and  False) #False
# print(True or  False) #True

# a = 10
# b = 20
# print(a < b and b > 15) #True

# print(not(False)) #True 

# print(True and not False) 




# class FoodOrder:   
#     platform_name = "OrderZone"

#     def __init__(self, CN,FN,QU,PR):
#         self.customer_name = CN
#         self.food_item = FN
#         self.quantity = QU
#         self.price = PR

#     # Method to display order details
#     def display_order(self):
#         # Local variable
#         total_bill = self.quantity * self.price

#         print("----- Food Order Details -----")
#         print("Customer Name :", self.customer_name)
#         print("Food Item     :", self.food_item)
#         print("Quantity      :", self.quantity)
#         print("Price         : ₹", self.price)
#         print("Total Bill    : ₹", total_bill)
#         print()



# order1 = FoodOrder("Nani", "Biriyani", 2, 460)
# order2 = FoodOrder("Sai", "Pizza", 1, 350)
# order3 = FoodOrder("Lohi", "Burger", 3, 300)
# order4 = FoodOrder("Gayatri","Chiken Fry Biriyani",4,720)

# order1.display_order()
# order2.display_order()
# order3.display_order()
# order4.display_order()

# print("Platform Name (Using Class):", FoodOrder.platform_name)
# print("Platform Name (Using Object):", order1.platform_name)







fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
costs = [120, 180, 60, 100, 150]

highest_cost = max(costs)
highest_fruit = fruits[costs.index(highest_cost)]

print("Highest Cost Fruit:", highest_fruit)
print("Cost: ₹", highest_cost)