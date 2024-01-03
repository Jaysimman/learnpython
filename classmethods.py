class laptop():
    chargertype="C-TYPE"
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self, price): #instance method
        self.price=price
    def getprice(self):
        print (self.price)
    @classmethod  #classmethod
    def changechargertype(cls):
        cls.chargertype="B-Type"
        print("Charger Type changed to B")
    @staticmethod #static method
    def info():
        print("This is laptop class")
hp=laptop()
hp.getprice()
hp.setprice(30000)
hp.getprice()
hp.info()
laptop.changechargertype()