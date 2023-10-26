#functions in python
#string  transform functions
#capitalize
message = "hi, how are you?"
print(message.capitalize())

#title
name = "manohar jumbarathi"
print(name.title())

#upper
name = "manohar jumbarathi"
print(name.upper())

#lower
name = "MANOHAR JUMBARATHI"
print(name.lower())

#casefold
name = "MANOHAR JUMBARATHI@10"
print(name.casefold())

#swapcase
name = "MANOHAR JUMBARATHI"
print(name.swapcase())

name = "manohar jumbarathi"
print(name.swapcase())

#string check functions

#isnumeric
a = "12234"
print(a.isnumeric())

#isalnum
a = "manohar10"
print(a.isalnum())
b = "manohar"
print(b.isalnum())

#isdigit
a = "235"
print(a.isdigit())

#isasscii
a = "G4G"
print(a.isascii())

#isupper
a = "MANOHAR JUMBARATHI"
print(a.isupper())

#islower
a = "manoharjumbarathi"
print(a.islower())

#isspace
a = " "
print(a.isspace())

b = "prasad"
print(b.isspace())

#isidentifier
a = "manohar jumbarathi"
print(a.isidentifier())

#isprintable
a = "manohar jumbarathi101"
print(a.isprintable())

#istitle
a = "Hello, Welcome!"
print(a.istitle())

#string len function
name = "manohar jumbarathi"
print(len(name))

#string search functions

#index
email = "manoharjumbarathi10@gmail.com"
print(email.index("1"))
print(email.index("@"))

#rindex
email = "manoharjumbarathi10@gmail.com"
print(email.rindex("0"))
print(email.rindex("@"))

#find
email = "manoharjumbarathi10@gmail.com"
print(email.find("0"))
print(email.find("b"))

email = "manoharjumbarathi10@gmail.com"
print(email.find("1"))
print(email.find("@"))

#rfind
email = "manoharjumbarathi10@gmail.com"
print(email.rfind("1"))
print(email.rfind("@"))

#startswith
email = "manoharjumbarathi10@gmail.com"
print(email.startswith("manohar"))
print(email.startswith("10"))

#endswith
email = "manoharjumbarathi10@gmail.com"
print(email.endswith("manohar"))
print(email.endswith(".com"))

#CRUD functions
#create/add data
#append
lst = []
lst.append("manohar")
lst.append("25")
print(lst)

#insert
names = ["a", "b", "c"]
names.insert(2, "manohar")
print(names)

#read
names = ["a", "b", "c"]
print(names.index("b"))

#count
names = ["a", "b", "c", "a"]
print(names.count("a"))

#extend
names = ["a", "b", "c"]
num = ["1", "2", "3"]
names.extend(num)
print(names)

#remove
names = ["manohar", "jumbarathi", "10"]
names.remove("jumbarathi")
print(names)

#pop with index
names = ["manohar", "jumbarathi", "10"]
names.pop(2)
print(names)

#pop without index
names = ["manohar", "jumbarathi", "10"]
names.pop()
names.pop()
print(names)

#clear
names = ["manohar", "jumbarathi", "10"]
names.clear()
print(names)

#sort
num = [8, 3, 5, 2, 6, 1]
num.sort()
print(num)

#reverse
num = [8, 3, 5, 2, 6, 1]
num.reverse()
print(num)
