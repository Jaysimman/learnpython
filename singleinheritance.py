#Single inheritance:
class dad():
    def phone(self):
        print("Dad's phone")
class son(dad):
    def laptop(self):
        print("Son's laptop")
ram=son()
ram.laptop()
ram.phone()