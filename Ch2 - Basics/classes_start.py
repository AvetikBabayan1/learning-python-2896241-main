#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini

class Xanut():
    def __init__(self, anun):
        self.anun = anun

class Red_Zone(Xanut):
    def __init__(self,discount):
        super().__init__("Red_Zone")
        self.manager = "Manager"
        self.discount_quantity = 1000
        self.discount=discount

class Bazaar(Xanut):
    def __init__(self, discount, hasDiscount):
        super().__init__("Bazaar")
        if (hasDiscount):
            self.discountPr = 0.85
        else:
            self.discountPr = 1
        self.discount=discount

redzone1 = Red_Zone(0.9)
redzone2 = Red_Zone(0.75)
bazaar1= Bazaar(0.6, True)

print(redzone1.discount)
print(redzone2.anun)
print(bazaar1.discount)
