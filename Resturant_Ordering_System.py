import sys
class MenuItem:
    def __init__(self):
        self.__total_price = 0
        self.__chosen_item = []
        print(self.menu())
        
        while True:
            self.choosing_category()
            self.categories()
            self.choosing_item()
            self.foodItem()
        

    def menu(self):
        return """
========== 🍴 Food Café Menu 🍴 ==========

🥪 Sandwiches
---------------------------------
Veg Sandwich ............ ₹80
Grilled Cheese .......... ₹120
Chicken Sandwich ........ ₹150
Club Sandwich ........... ₹180

🍕 Pizza
---------------------------------
Margherita .............. ₹200
Veggie Delight .......... ₹250
Pepperoni ............... ₹300
BBQ Chicken ............. ₹350

☕ Beverages
---------------------------------
Espresso ................ ₹100
Cappuccino .............. ₹120
Cold Coffee ............. ₹150
Green Tea ............... ₹80

🍰 Desserts
---------------------------------
Brownie ................. ₹90
Cheesecake .............. ₹150
Ice Cream (2 scoops) .... ₹100
Chocolate Muffin ........ ₹70

=========================================
"""
        
    def choosing_category(self):
        self.category = int(input("""Please Choose The Category you want to order from: 
              1. Sandwiches
              2. Pizza
              3. Beverages
              4. Desserts 
              5. Quit \n"""))
        
    def sandwiches(self):
        self.sandwiches_items = {
    1: {"Veg Sandwich": 80},
    2: {"Grilled Cheese": 120},
    3: {"Chicken Sandwich": 150},
    4: {"Club Sandwich": 180},
}
        return self.sandwiches_items


    def pizza(self):
        self.pizza_items = {
    1: {"Margherita": 200},
    2: {"Veggie Delight": 250},
    3: {"Pepperoni": 300},
    4: {"BBQ Chicken": 350},
}
        return self.pizza_items
    
    def beverages(self):
        self.beverages_items = {
    1: {"Espresso": 100},
    2: {"Cappuccino": 120},
    3: {"Cold Coffee": 150},
    4: {"Green Tea": 80},
}
        return self.beverages_items


    def dessert(self):
        self.dessert_items = {
    1: {"Brownie": 90},
    2: {"Cheesecake": 150},
    3: {"Ice Cream (2 scoops)": 100},
    4: {"Chocolate Muffin": 70},
}
        return self.dessert_items

    def categories(self):
        
        if self.category == 1:
            print(self.sandwiches())
            
        elif self.category == 2:
            print(self.pizza())
            
        elif self.category == 3:
            print(self.beverages())
            
        elif self.category == 4:
            print(self.dessert())
            
        elif self.category == 5:
            sys.exit()
        
        else:
            print("Your Input is Wrong please Choose from 1 to 5")
        
    
    def choosing_item(self):
        self.item = int(input("Please Choose the food Item from 1 to 4 from the chosen Category: \n"))
        return self.item
              
    def foodItem(self):
        
        self.categ = {
            1: self.sandwiches(),
            2: self.pizza(),
            3: self.beverages(),
            4: self.dessert()
        }

        food_dict = self.categ.get(self.category)
        if food_dict and self.item in food_dict:
            food_name = list(food_dict[self.item].keys())[0]
            food_price = list(food_dict[self.item].values())[0]

            print(f"You ordered {food_name} for Rs {food_price}")
            self.__chosen_item.append(food_name)
            self.__total_price += food_price
        else:
            print("Your Input is Wrong please Choose from 1 to 4")
        print(f"your total bill is Rs {self.__total_price}")

obj = MenuItem()
