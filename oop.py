class Item:
    pay_rate = 0.8  # pay rate after a 20% discount
    all = []

    def __init__(self, name: str, price: float, quamtity=0):
        # Run validations to the arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quamtity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.Quantity = quantity

        # Actions to excecute
        Item.all.append(self)

        def calculate_total_price(self):
            return self.price*self.quantity

        def apply_discount(self):
            self.price = self.price * self.pay_rate

            def __repr__(self):
                return f"Item({self.name}", {self.price}, {self.quantity}

                item1 = Item("phone", 100, 1)
                item2 = Item("laptop", 1000, 3)
                item3 = Item("cable", 120, 6)
                item4 = Item("mouse", 290, 2)
                item5 = Item("keyboard", 9000, 7)

                print(Item.all)

                # OOP helps the structure of the code by grouping related data and behaviurs intto the objects.You start by defining classes, which are blueprints for creating objects. Each object can have its own attributes (data) and methods (functions) that operate on that data. This encapsulation makes the code more organized and easier to manage, especially as the complexity of the application grows.and the creates objectsfro them.
                # The key concepts of OOP in python are encapsulation, inheritance, abstaraction and polymorphism.
                # When creating a class is like creating a variable eg , lets say our class is called dog, then we can create an object called Tiny, Fido, etc. These objects will have the same attributes and methods as defined in the class Dog.
                # Attributes are a collection of variables.
                # Methods are a collection of functions. To add methods you must add them to the class definition.Attributes are also added to the class definition but can also be added to the object definition.
                # To declare a class in python:

                Class ClassName:
                "This is a class docstring that describes the class functionality."
                "<Do stuff here>"
                # END
                # For example
                Class Dog:
                """This is a class that represents a dog."""

                def bark(self):
                    """Make the dog bark."""
                    print("Woof!")
                    Dog1 = Fido()
                    Dog2 = Tiny()

                    # To add attributes to the class, you can define them in the __init__ method, which is called when an object is created. For example:
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age
                        # To add methods to the class, you can define them as functions within the class. For example:

                        def bark(self):
                            print(f"{self.name} says Woof!")
                            # To instantiate the class, you create an object of that class by calling the class name as if it were a function. For example:
                            my_dog = Dog("Buddy", 3)
                            # The _str() method is used to control what is being returned when the class object is called as a string.
                            # The initialization method __init__ is a special method that is automatically called when an object of the class is created.
                            # It allows you to set initial values for the object's attributes.

                            def _init__(self, name, age):
                                self.name = name
                                self.age = age
                                # End innit method.

                                # Docstrings are used to provide documentation for the class and its methods.
                                # They are enclosed in triple quotes and can be accessed using the __doc__ attribute of the class or method.example:
                                Class Dog:
                                """This is a class that represents a dog."""

                                def move(self, a, b):
                                    "move the dog to a new position"
                                    self.fido = a
                                    self.tiny = b
                                    # End move
                                # End class Dog
