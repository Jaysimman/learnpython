class phone():
    chargertype="C-Type"#This is called class variable
    def __init__(self,brand,price):
        self.brand=brand##this is called instance variable
        self.price=price
    def display(self):
        print("Brand : ",self.brand)
        print("Price : ",self.price)
        print("Charger Type : ",self.chargertype)
phone.chargertype="B-Type"
samsung=phone("Samsung",10000)
samsung.display()
print()
redmi=phone("Redmi",5000)
redmi.display()