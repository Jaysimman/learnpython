class school:
   print("---------------Welcome to SRVMHSS--------------- ")
   print()
   name = ""
   age = 0
   roll_no = 0
   sex = ""
   
   def __init__(self):
      print("---------------The information of the student is---------------")
      print()

   def marks(self):
      print()
      tamil = int(input("Enter a Tamil Mark: "))
      english = int(input("Enter a English marks: "))
      maths = int(input("Enter a maths mark: "))
      science = int(input("Enter a science mark: "))
      social_science = int(input("Enter a Socail science mark: "))
      self.total = tamil + english + maths + science + social_science

   def grade(self):
      print("The total mark is: ",self.total)
      percent = int(self.total/5)
      print()
      print("The student total percentage is : ",percent)
      print()
      if percent <= 90 and percent>=100:
         print("Pass with O grade")
      elif percent <=80 and percent>=89:
         print("Pass with A grade")
      elif percent <=70 and percent>=79:
         print("Pass with B grade")
      elif percent <=60 and percent>=69:
         print("Pass with C grade")
      elif percent <=50 and percent>=59:
         print("Pass with D grade")
      elif percent <=40 and percent>=49:
         print("Pass with E grade")
      elif percent >=39:
         print("Sorry Student Failed")

jai = school()

jai.name = "Jay"
jai.age = 21
jai.roll_no = 20115020
jai.sex = "Male"

print("Student name is : ",jai.name)
print("Student age is : ",jai.age)
print("Student roll no is : ",jai.roll_no)
print("Student Gender is : ",jai.sex)

jai.marks()
jai.grade()