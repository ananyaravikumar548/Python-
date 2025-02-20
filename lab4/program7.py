#initializing dictionaries
BCA = { "USN":"0010", "Name":"Amrithaa", "USN2":"0011","Name2":"Ananya"}
print(BCA)
#Printting only either keys or values 
# print(BCA.keys())
# print(BCA.values())
for key in BCA:
    print(key)
    print(BCA[key])
  #Adding a new key and value to the dictionary
#BCA["USN3"]=["0069"]
#BCA["Name3"]=["Prateeksha"]
BCA.update({"USN3":"0000", "Name3":"XYZ"})
print(BCA)

if "Name3" in BCA:
    print(True)
#Printting only either keys or values 
# print(BCA.keys())
# print(BCA.values())
for key in BCA:
    print(key)
    print(BCA[key])
