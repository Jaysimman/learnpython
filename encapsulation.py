class company():
    def __init__(self):
        self.__companyname="Google"#it becomes private variable
    def companyname(self):
        print(self.__companyname)
c1=company()
c1.companyname()
#print(c1.__companyname)

#protected variable

class college():
    def __init__(self):
        self._studentname="Jai" #single _ stands for protected and its accessable outside of a class and inside of a class function
class b(college):
    pass
bb=b()
print(bb._studentname)