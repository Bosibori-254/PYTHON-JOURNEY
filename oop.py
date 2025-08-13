class Item:
        pay_rate = 0.8  # pay rate after a 20% discount
        all = []

        def __init__(self, name: str, price: float, quamtity=0):
                # Run validations to the arguments
                assert price >= 0, f"price {price} is not greater than or equal to:
                assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to:

                #Assign to self object
                self.name= name
                self.price = price
                self.Quantity= quantity

                #Actions to excecute
                Item.all.append(self)

                def calculate_total_price(self):
                    return self.price*self.quantity
                
                def apply_discount(self):
                    self.price = self.price *self.pay_rate

                    def __repr__(self):
                        return "fItem("{self.name}",{self.price}, {self.quantity})"

                        item1 = Item("phone" , 100, 1)
                        item2 = Item("laptop", 1000. 3)
                        item3 = Item("cable", 120, 6)
                        item4 = Item("mouse", 290, 2)
                        item5 = Item("keyboard", 9000, 7)

                        print(Item.all)
                        




                        
                        
            

