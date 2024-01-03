#multilevel inheritance
class grandpa():
    def phone(self):
        print("grandpa's phone")
class dad(grandpa):
    def money(self):
        print("Dad's money")
class son(dad):
    def laptop(self):
        print("Son's laptop")
ram=son()
ram.laptop()
ram.money()
ram.phone()
print()
appa=dad()
appa.money()
appa.phone()