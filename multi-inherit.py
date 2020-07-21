# Base Class
class Product:

    def __init__(self, title):
        # self.price = 0 <-- we don't need this now
        self.title = title
        self.description = ""

    # getter
    @property
    def price(self):
        try:
            return self.__price # Note there are 2 underscores here
        except AttributeError:
            return 0


    # setter
    @price.setter
    def price(self, new_price):
        if type(new_price) is float:
            self.__price = new_price
        else:
            raise TypeError("Please provide a floating point value for the price.")

# A base class AND a child class
class Coat(Product):

    def __init__(self, title):
        super().__init__(title)

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"

# More base classes to help us fine tune whether a product is on sale or a featured item with a markup price
class SaleItem:

    def __init__(self, discount):
        self.discount = discount


class FeaturedItem:

    def promote(self):
        print(f"{self.title} will make your neighbors green with envy! Buy one for your dog!")


# Derived classes using multiple inheritance
class ClearanceCoat(Coat, SaleItem):

    def __init__(self, title, discount ):
        # Cannot use super() with multi-inheritance
        Product.__init__(self, title)
        SaleItem.__init__(self, discount)

    @property
    def discount_price(self):
        discount = self.price * (1 - self.discount)
        return f'${discount:.2f}'


class CoolShoes(Product, FeaturedItem):

    def __init__(self, title):
        Product.__init__(self, title)

    @property
    def premium_price(self):
        premium = self.price * 1.2
        return f'${premium:.2f}'

summerCoat = ClearanceCoat("GoreTex SubZero Ski Jacket", .25)
summerCoat.price = 125.00
print("discounted coat", summerCoat.discount_price)

# **************************************************************
# Example #2
# Base, or parent, class
class Employee:

    def __init__(self, name=""):
        self.name = name
        self.title = ""
        self.start_date = ""

    def pay_employee(self):
        print(f"Yay! Now {self.name} can pay rent.")

    def take_vacation(self):
        print(f"{self.name} takes a nice, paid vacation")

    def __str__(self):
        return f"This is an employee named {self.name}"


# Derived, or, child, class
class SalariedEmployee(Employee):

    # We don't execute this dunder method
    def __init__(self, name, wage=0):
        # call the parent's __init__
        super().__init__(name)
        self.yearly_wage = wage


class ContractEmployee(Employee):

    # We don't execute this dunder method
    def __init__(self, name, wage=0):
         # call the parent's __init__
        super().__init__(name)
        self.hourly_wage = wage

    # method overriding
    def take_vacation(self):
        print(f"{self.name} takes an unpaid trip.")


class Remote:

    def __init__(self, stipend=0):
        self.tech_stipend = stipend


class OnSite:

    def __init__(self, cubicle_number):
        self.__cubicle_number = cubicle_number

    @property
    def cubicle_number(self):
        return self.__cubicle_number

    @cubicle_number.setter
    def cubicle_number(num):
        if num != self.__cubicle_number:
            self.__cubicle_number = num
        else:
            print("Employee already assigned to that cubicle. Try a different soul-sucking location.")

# Child class that inherits from multiple classes
class RemoteSalaried(Remote, SalariedEmployee):

    def __init__(self, name, wage, stipend):
        Remote.__init__(self, stipend=stipend)
        SalariedEmployee.__init__(self, name, wage=wage)

    def calcMonthlyTakehome(self):
        total = self.yearly_wage / 12 + self.stipend
        return f"{self.name} earns {total} per month"
