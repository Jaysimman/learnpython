a={"name":"Jai",
   "age":"21",
   "loc":"Tiruppur",
   "f_members":["appa","amma","thambi",1,2,3]}
print(a)
print(a["name"])
print(a["loc"])
print(a.keys())
print(a.values())
a["age"]=22
print(a)
a["colour"]="red"
print(a)
a.update({"age":2})
print(a)
a.pop("age")
print(a)
del a["name"]
print(a)# we can able to delete a dict using "del a"
a.clear()#used to clear a value
print(a)