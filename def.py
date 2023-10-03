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