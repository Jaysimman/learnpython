def paint(msg):
   print("Message",msg)
paint("paint my house")

def add():
   a = int(input("Enter a number1: "))
   b = int(input("Enter a number2: "))
   print(a+b)
add()
def sub():
   a = int(input("Enter a number3: "))
   b = int(input("Enter a 4: "))
   print(a-b)
sub()
number = int(input("Enter a number:4 "))
def findoddoreven(b):
   if(b%2==0):
      print("Even")
   else:
      print("Odd")
findoddoreven(number)
def painter():
   return 20
msg = painter()
print(painter())
print(msg)

s_usrname = "jai"
s_pass = "123"

u_name=input("Enter a user name: ")
u_pass=input("Enter a password: ")

def validate():
   if(u_name== s_usrname and u_pass == s_pass):
      print("Correct")
      return True
   else:
      print("Wrong")
      return False
validate()
print(validate())