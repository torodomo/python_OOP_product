# The owner of a store wants a program to track products. Create a product class to fill the following requirements.


class product(object):

    def __init__(self, price, item_name, weight, brand, cost, tax, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        self.tax = tax
        if self.status != "for sale":
            self.status == "sold"

        if self.status == "used":
            self.price = self.price * .80

        if self.status == "sold":
            self.price = 0
        
       
    def displayAll(self):
        print "Item Name:", self.item_name
        print "Brand:", self.brand
        print "Price: $", self.price
        print "Tax rate:", self.tax, "%"
        print "Total Price: $", round(self.price * self.tax, 2)
        print "Weight:", self.weight, "lb"
        
        print "Status", self.status
        return self
    
    



product1 = product(99.99,"abc",23, "domo", 20, 1.5, "used")
product1.displayAll()
