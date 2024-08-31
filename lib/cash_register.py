#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity  # x+=3 == x=x+3

        for _ in range(quantity):       #when you dont want the value being iterated over
            self.items.append(item)
            
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

    # applies discount
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")


    #  method will remove the last transaction from the total. 
    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void." #checks if the previous_transactions list is empty.
        
        self.total -= (
            self.previous_transactions[-1]["price"] * self.previous_transactions[-1]["quantity"]
        )

        for _ in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
        self.previous_transactions.pop()


# add item................................................................
register= CashRegister(discount = 0) 
register.add_item("chapati", 20, 5)
print(register.total)  
print(register.items)   
print(register.previous_transactions)   

# discount...............................................................
register.apply_discount()





        
    
    
    
