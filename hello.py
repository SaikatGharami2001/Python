import math
import random
import copy

# Hello this is my very first python code!
# print("Hello!")

# print("Trippin'")  # Hey there this is how to print in python

# print("Python also accepts single brackets for for printing")

# print("This is how to  break line in python \n'Broke!'")

# print("Path : C:\\Images\\RealImages")

# print("This is how to print a tab in \t python ")

## Challenge Output

# print(
#    """Your Learning Path :
#       \t - Python Basics
#       \t - Data Engineering
#       \t - AI"""
# )


age = 24
heightInCentimeters = (5 * 12 + 10) * 2.54
myName = "Saikat"
isStudent = False
something = None

# print(age, heightInCentimeters, myName, isStudent, something)


# print(type(age))
# print("Saikat is " + str(age) + " years old")
age = str(age)
# print(type(age))

text = """  
  Saikat is learning Python
 Saikat will soon finish python
  """

# print(text.count("Python"))
# print(text)

price = "123,45"
newPrice = price.replace(",", ".")
# print(newPrice)

phone = "+49 (176) 123-45667"

clearPhone = (
    phone.replace("+", "00")
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
    .replace(" ", "")
)
print(phone)
print(clearPhone)

firstName = "Saikat"
lastName = "Gharami"
lastName = firstName + " " + lastName
# print(lastName)

status = "RICH"

# print(f"Saikat will be {status}")

data = "Saikat-24-India"
# print(data.split("-"))
# print(data)

value = "$" * 30
# print(value)

date = "20260903"

num = " 2"
num2 = 2
# print(num.strip())
# print(num)

result1 = num.startswith(" ")
result2 = num.endswith("2")
result3 = date.isnumeric()

# print(3 / 2)
# print(3 // 2)
# print(3**2)

# print(4.3)
# print(abs(-4.3))

a = 3.3

# print("Phew", math.trunc(a))

b = random.random()
# print(b)

c = random.randint(1, 100)
# print(c)

# print(c % 2 == 0)

phone = "+9384-390849-309480"
phone2 = "+93-93843-394839"

finding = phone.find("-")
finding2 = phone2.find("-")
# print(phone[finding + 1 :])
# print(phone2[finding2 + 1 :])

b = 3.2
# print(b.is_integer())

randomNumber = random.random()
# print(randomNumber)

rNum = random.randint(1, 10)
# print(rNum)

ins = isinstance(rNum, float)
# print(ins)

isEven = random.randint(1, 100)
# print(isEven)
# print(isEven % 2 == 0)

# print(bool(1))

# print(bool())

# print(bool(""))

# print(bool("-1"))

email = ""
phone = "+91-92783"
username = "Saikat"

tripping1 = any([email, phone, username])
tripping2 = all([email, phone, username])
tripping3 = any([email, phone, username])

# print(tripping2)

new = "Hello"
# print(new.startswith("h"))

aa = 10
bb = 10

# print(aa >= bb and bb > aa)

login = True
guest = False
banned = True

# print((login or guest) and not banned)

domain = "g.com"
banned_domain = ["g.com", "goodbutfake.com", "duplicate.com"]

# check = domain not in banned_domain
# print(check)
# print(domain in banned_domain)

x = [1, 2, 3]
y = [1, 2, 3]
# print(x is y)

x1 = [1]
y1 = [1]
# print(x1 is y1)


# Check if a user’s name is not empty and the age is greater than or equal to 18

userName = "f"
age = 33

# print(userName != "" and age >= 18)

# Check if the password is at least 8 characters long and does not contain spaces

password = "                 Hello@1234                       "
p = password.strip()
checkPass = len(p) >= 8 and " " not in p
# print(checkPass)

# Check if a user’s email is not empty, contains '@', and ends with '.com'

email = "Saikat@gmail.com"
contains = "a" in email

# print(
# f"Is 'a' contains in this emails : {contains} \nAlso ends with '.com' : {email.endswith(".com")}"
# )

# Check if a username is a string, is not None, and is longer than 5 characters

name = "Saikat"
isString = isinstance(name, str) and name is not None and len(name) > 5
# print(isString)

# Check if the user is either an admin or a moderator, and either they’re not banned or they’ve verified their email

user = "Admin"
banned = True
emailVerification = "Done"

# print(
#     f"The user is  :{ user } and is banned ? {banned}\nDid the user had completed the email verification ? {emailVerification}"
# )


score = 0
submitted_project = False

# if score >= 90 and submitted_project:
#     print("Very Good")
# elif score >= 90:
#     print("Good")
# elif score >= 80:
#     print("Average")
# elif score >= 70:
#     print("Okay")
# elif score >= 60 or submitted_project:
#     print("Just Okay")
# else:
#     print("Failed")

# phew = "A" if score == 0 else "B"
# print(phew)

# country = "USA"

# match country:
#     case "United States" | "USA":
#         print("US")
#     case "India":
#         print("IN")
#     case "Germany":
#         print("DE")
#     case _:
#         print("Unknown Country")

# Must not be empty
# Must contain '.' and '@'
# Must contain exactly one '@' symbol
# Must end with '.com', '.org', or '.net'
# Must not be longer than 254 characters
# Must start and end with a letter or digit

# email = "Saikatgharami2@gmail.com"
# email = email.strip()

# if not email:
#     print("Email must not be Empty")

# if not ("." in email and "@" in email):
#     print("Email must contain . and @")

# elif email.count("@") != 1:
#     print("Email must contains only 1 @")

# if not email.endswith((".com", ".org", ".net")):
#     print("Email must ends with the mentioned ending")

# if len(email) > 254:
#     print("Must not be longer than 254 chars")

# if not (email[0].isalnum() and email[-1].isalnum()):
#     print("Must starts with letter or digit")
# else:
#     print("Valid Email")

# password = 1

# # Must not be empty
# if not password:
#     print("Password can't be empty")

# # Must be at least 8 characters
# if not len(password) >= 8:
#     print("Password must be longer than 8 chars")

# # Must include at least 1 uppercase
# if not password.count(password.uppercase()):
#     print("Must include at least 1 uppercase")

# # Must include at least 1 lowercase


# # Must not be same as the email
# if password == email:
#     print("Password must not be same as email")

# # Must not contain any spaces
# if " " in password:
#     print("Password must not contain any spaces")

# # Must start and end with a letter or digit

# if not (password[0].isalnum() and password[-1].isalnum()):
#     print("Must start and end with a letter or digit")

# items = (
#     1,
#     2,
#     3,
#     4,
#     1,
# )

# for item in range(2, 10 + 1, 2):
#     print(item)


# scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0

# for score in scores:
#     total = total + score
#     print(f"Current score is {total}")
# print(f"Final score is {total}")

# files = ["  Report.pdf", "DATA.pDF", "PHeW.eDf"]

# for file in files:
#     file = file.strip().lower().replace("edf", "pdf")
#     print(file)

# table = 7

# for i in range(1, 11):
#     print(f"{table} * {i} = {table * i}")

# star = "*"

# for i in range(1, 7):
#     print(star * i)

# names = ["Newly", "Newish", "", "Phew"]

# for name in names:
#     if name == "":
#         print("Empty Found!")
#         print("Values are :", name)
#         continue
#     print("Values are ", name)

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# # Skip the weekends

# for day in days:
#     if day in ["Saturday", "Sunday"]:
#         continue
#     print(day)

# emails = ["data@gmail.com", "data@yahoo.com", "DROP TABLE USERS;", "data@data.com"]

# for email in emails:
#     if ";" in email:
#         continue
#     print(email)

# items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in items:
#     if i % 2 != 0:
#         print(f"Even numbers are : {i}")
#         break
# else:
#     print("All the numbers are odd")

# names = ["Raja", "Munna", "Mousumi", "Sudhanshu"]

# for name in names:
#     if name == None:
#         print("Found a Missing Data which is", name)
#         break
# else:
#     print("All names are present")

# years = [2026, 2027]
# months = ["Jan", "Feb"]
# days = range(1, 29)

# for y in years:
#     for m in months:
#         for d in days:
#             print(f"Days are {d}, Months are {m} and the years are {y}")

attempts = 0
# answer

# while attempts < 3:
#     answer = input("Yes or no ?")
#     if answer == "Yes":
#         print("Glad we're on the same page")
#         break
#     attempts += 1
# else:
#     print("All 3 attempts")

# count = 1

# while True:
#     if count > 3:
#         print("All 3 attempts Done")
#         break

#     answer = input("Yes or no ? ")
#     if answer == "Yes":
#         print("Glad we're on the same page")
#         break

#     count += 1
# else:
#     print("Thank you")

# empty = [1, 2, 3, 4, 5, True, "c"]
# print(empty)
# print(type(empty))

# empty = list()
# print(empty)

# letters = list("Python")
# print(letters)

# range = list(range(5))
# print(range)

# matrix = ["a", "b", "c", "d", "e", "f"]
# matrix1 = ["a", "b", "c", "d", "e", "f"]

# print(matrix[:5])
# print(matrix[2:5])

# for mat in matrix:
#     print(mat)

# person = ["TCMS", "24", "Saikat"]

# school, age, name = person

# print(school)
# print(name)
# print(age)


# person = ["TCMS", "24", "Saikat", "Techm", "Gym Boy"]

# school, *details, company = person

# print(school)
# print(details)
# print(company)

# person = ["TCMS", "24", "Saikat", "Techm", "Gym Boy"]

# school, *details = person

# print(school)
# print(details)

# person = ["TCMS", "24", "Saikat", "Techm", "Gym Boy"]

# *school, details = person

# print(school)
# print(details)

# person = ["TCMS", "24", "Saikat", "Techm", "Gym Boy"]

# a, b, c, d, school, details = person
# ## Note the no of variables must match the values exactly - Not less, Not more
# print(a)
# print(b)
# print(c)
# print(school)
# print(details)


# person = ["TCMS", "24", "Saikat"]
# _, _, name = person
# print(_, _, name)


# person = ["TCMS", "24", "Saikat", "a", "a", "a"]

# phew, *_, name = person

# print(phew, _, name)

# numbers = [1, 2, 10, 49, 405]
# print("Max num is", max(numbers))
# print("Min num is", min(numbers))
# print("Sum of nums is", sum(numbers))
# print("Length of nums is", len(numbers))
# print(max([1, 2, 3]))

# print("All demo :", all([0, 2, 34]))
# print("Any demo :", any([0, 2, 34]))

# numbers = [1, 2, 10, 49, 49, 405, 1, -3]

# print("Count : ", numbers.count(1))
# print("Index : ", numbers.index(-3))

# numbers = [1, 2, 10, 49, 49, 405, 1, -3]

# print(4 in numbers)
# print(-3 in numbers)

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]

# print(list1 < list2)
# print(list1 is list2)  ## It checks memory reference is method does not check values

# list = [1, 2, 3]

# list.append(4)
# list.extend([4, 5, 6, 7])

# print(list)

# list = [1, 2, 4, 5]
# list.insert(2, 3)  # insert(position,value) NOT insert(value,position)

# print(list)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# matrix[1].insert(0, 1)
# print(matrix)

# letters = [1, 2, 3, 3, 3]

# letters.remove(3)
# letters.remove(3)
# print(letters)

# num = [1, 2, 3]
# removed = num.pop()
# print(removed)

matrix = [[1, 2, 3], [7, 8, 9], [4, 5, 6]]

# matrix[2].sort(reverse=True)

# phew = sorted(matrix)
# phew = sorted(matrix, reverse=True)

# print(matrix)

# matrix[0][0] = 0
# matrix[1][1] = 0
# matrix[2][2] = 0
# print(matrix)

# remove = matrix.remove([1, 2, 3])
# letters = ["a", "b", "c"]
# letters[0] = "x"

# letters = 2
# print(letters)
# print(type(letters))

# removed = letters.pop()
# print(removed)

letter = ["a", "b", "c", "d"]

# letter.reverse()
# print(letter)

# new_list = list(reversed(letter))
# print(new_list)

# letter.sort()
# print(letter)
# letter.sort(reverse=True)
# print(letter)

# letters = ["a", "b", "c"]
# new_letters = letters.copy()
# new_letters.append("d")
# print(letters)
# print(new_letters)

# matrix = [[1, 2, 3], [4, 5, 6]]
# matrixCopy = matrix.copy()  # Shallow Copy

# matrix[0].append("3")
# print(matrixCopy)
# print(matrix)

# matrix = [[1, 2, 3], [4, 5, 6]]
# matrixCopy = copy.deepcopy(matrix)  # Deep Copy
# matrix[0].append(3)
# matrix.pop()
# print(matrix)
# print(matrixCopy)

# original = [[1, 2], [1, 2]]
# copy = original.copy()

# sharing = copy[0] is original[0]
# print(sharing)

# letters = [1, 2, 3]
# letters.extend([4, 5, 6])
# newList = ["a", "b", "c", "d"]
# print(list(zip(newList, letters, "Phew")))

letter = ["b", "a", "c"]
news = []

# for l in letter:
#     news.append(l.upper())
#     print(news)

# print(news.append("a"))

# a = [1, 3, 5]
# b = [2, 4, 6]
# print(list(zip(a, b)))

# a = [1, 2, 3, 4, 5, 6]

# for x in a:
#     print(x)

letters = ["rat", "phew", "cat"]
# okay = []

# for x in letters:
#     okay.append(x.upper())
#     print(okay)

# for index, pos in list(enumerate((letters))):
#     print(index, pos)

# water = ["a", "b", "c"]
# heat = [1, 2, 3]

# for l in zip(heat):
#     print(l)

# listing = ["a", "b", "c"]
# mapping = list(map(str.upper, listing))
# print(mapping)

# #  OR

# nums = ["1", "2", "3"]

# phew = list(map(int, nums))
# print(phew)

# names = ["ABC ", " DEF", "   GHL"]

# for n in map(str.strip, names):
#     print(n)

# chars = ["a", "b", "", " ", None, False]
# filtered = list(filter(None, chars))
# print(filtered)

# words = ["1", "3", "Saikat"]
# filtering = list(filter(str.isalpha, words))
# print(filtering)

# # OR

# for i in filter(str.isalpha, words):
#     print(i)

# multiple = lambda x, y: y * (x + 1)
# print(multiple(2, 2))

# checking = lambda x: x in "Saikat"
# print(checking("b"))

# prices = ["$1.1", "$2.2", "$3.3"]
# result = list(map(lambda x: x.replace("$", ""), prices))
# print(result)

# Filter prices below 100

# prices = [1, 2, 300, 300, 100, 400]
# result = list(filter(lambda x: x > 100, prices))
# print(result)

# students = [["Raja", 10], ["Sagar", 20], ["Saikat", 30]]
# result = list(map(lambda x: x[1] > 10, students))
# print(result)

# names = [["Maria", 22], ["Saikat", 24], ["Jennie", 23]]
# sandwich = list(filter(lambda x: x[0].startswith("M"), names))
# print(sandwich)

# domain = ["www.google.com", "www.localhost", "www.openai.com", "Phew"]
# clearData = [d.lower().replace("www.", "") for d in domain if "." in d]
# print(clearData)


# --------


#  There are total 4 data structures in py , List , Tuple , set , dict(dictionary)

# 1: List []

my_list = [10, 20, 30, 10]
# print(my_list)  # Ordered # Allow Duplicates
# print(my_list[1])  # Indexed
my_list[1] = 2  # Mutating
# print(my_list.pop()) # Mutating
# print(my_list)  # Mutable

# List :
# Are order based
# Allow duplicate
# Are index based
# Are mutable

# --------


# 2: Tuple ()


# Tuple is a ordered collection that can't be changed after creating it
# Allow duplicate
# Are index based
# Are Not mutable

my_tuple = (10, 30, 20, 100)

# print(my_tuple)  # Allow duplicate # Are order based
# print(my_tuple[1])  # Are index based

# my_tuple[1] = 1
# print(my_tuple)  # Are Not mutable
# my_tuple.remove() # Will not work since it is immutable
# my_tuple.pop() # Will not work since it is immutable
# my_tuple.add() # Will not work since it is immutable

# print(
#     sorted(my_tuple)
# )  # After doing this operation the output is a list not a tuple anymore hence it is immutable


# --------


# 3: sets {}
# Unordered collection of unique values
# Not order based
# Not Allow duplicate
# Not index based
# Are mutable

my_set = {30, 20, 100}

# Set methods
# How to add value to our set ? We can't use append or insert here coz those are based on the position number of the data
# We can only add unique values since set does not allow duplicates
my_set.add(-10)
# my_set.update("10")  # ✅ Only allows iterable values
# my_set.update(10)  # ❌ Not allows non iterable values
my_set.update({1, 2})
my_set.update([3, 9])

# Update methods shortcut
# Instead of my_set.update we can write |=
my_set |= {90}

# my_set.remove(90)  # Only removes if the value is present, if not error
my_set.discard(900)  # Better way to remove values from a set without any error

# print(my_set)

# Sets mathematical operations
# Addition
new_set = {1, 2, 3, 4}
addingInSet = new_set.union({5, 7})
# OR
addingInSet2 = new_set | {5, 7}  # Same thing

# print(new_set)
# print(addingInSet)
# print(addingInSet2)

# Intersection

# value1 = {1, 2, 3, 4}
# value2 = {3, 4, 5, 6}

# print(value1.intersection(value2))
# # OR
# print(value1 & value2)

# Difference

# value1 = {1, 2, 3, 4}
# value2 = {3, 4, 5, 6}

# print(value2 - value1)  # {5, 6}
# print(value1 - value2)  # {1, 2}

# Symmetric Difference

# value1 = {1, 2, 3, 4}
# value2 = {3, 4, 5, 6}

# print(value1.symmetric_difference(value2))
# # OR
# print(value1 ^ value2)

# value1 = {1, 2, 3}
# value2 = {3, 4, 5, 6}
# subset = value1.issubset(value2)
# # print(subset)

# checking = value1.isdisjoint(value2)  # To checking uniqueness
# print(checking)


# --------

# dict

my_dict = {"a": 1, "a": -2, "b": -2, "c": 3}

# Keys are unique and the values allows duplicate
# Dictionary cannot be indexed like my_dict[1] = 1 ❌
# But key's indexes works my_dict["b"] = 1 ✅

my_dict["b"] = 1
# print(my_dict["c"])  # Works and it is mutable
# print(my_dict)

# Dictionary methods

user = {
    "id": 1,
    "age": 21,
    "city": "Berlin",
}

# print(user["city"])

# # get() returns the value safely, gives None if missing

# print(user.get("name"))  # None

# # Or you can give a default value to the key

# print(user.get("name", "Isha"))  # None

# print("age" in user)
# print("name" not in user)


# View objects


# print(user.keys())  # Returns all the keys in your dictionary
# print(user.values())  # Returns all the values in your dictionary


# print(user.items())  # Returns all the keys , value pairs in your dictionary
# items() is perfect when you need key and value together fop looping, transforming data, building new dicts, comparing and more

# for u in user: # Gives only the keys
#     print(u)

# for u, i in user.items(): # Gives the full key and value pairs
#     print(u, i)

user["name"] = "Saikat"  # Add new value
user["age"] = 1  # Update old values

# Method update to update the dict values

# print(user)

user.update({"phew": "Phewing", "name": 20})  #  adds new, update old

# remove = user.pop("ids")  # Popping the not needful
# Problem with this method is if not present "ids" = error

# remove = user.pop("ids", "Not Found")  # Better way no error if not present

# If you want to pop the last item without mentioning the id then popitem works well

# print(user.popitem())

# print(user)

# If you want the create a new dict where the initial values are None or same then you can use the fromkeys()

# new_user = dict.fromkeys(["name", "age", "id"], None)
# new_user["name"] = "Mewing"
# print(new_user)

test = {
    "id": 3,
    "name": "Saikat",
    "age": 24,
    "city": "Berlin",
}


# Q. Create new dict, keep only the string pairs and make them upperCase

# testing = {k: v.upper() for k, v in test.items() if isinstance(v, str)}
# print(testing)

# -------

# Functions


# def real():
#     print("Real")


# i = 0
# for i in range(3):
#     real()

# import math

# print(len("Nigga"))
# print(round(9.1))


# def clear_name(my_name):
#     print(my_name.strip().upper())

# clear_name("             Saikat   ")


# def name(a, c, b="BU"):
#     print(a, b, c)


# name("AAA")

# If you do not know the no.of parameters then it is best to use the args


# def no(*args):
#     print(sum(args))


# no(1, 2, 3, 4)

# Create user profile


# def profile(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# profile(first_name="Phew", last_name="Phewing")  # Only works with keyword argument ✅
# # profile("Phew", "Phewing")  # Does not works with keyword argument❌


# def trippin(name):
#     low_name = name.strip().lower()
#     up_name = low_name.upper()
#     return low_name, up_name


# lower, upper = trippin("Saikat")
# print(lower)
# print(upper)

# ----- Task : store application log message in a file


def write_log(message):
    with open(r"E:\place.log", "a") as file:
        file.write(message + "\n")


# # write_log("Placing")
# write_log("Mewing")
# write_log("Phewing")


def clean_and_split_email(mail):
    cleared_mail = mail.strip().lower()
    name, domain = cleared_mail.split("@")

    return {"username": name, "domain": domain}


new_mail = clean_and_split_email("   BDMS@gmail.com")
# print(new_mail)


# --- Validation / checker functions ---

# Checks whether the password meets the minimum requirement of 8 chars


# def is_valid_pass(password):
#     if len(password) < 8:
#         return "Invalid Pass"
#     else:
#         return "Valid Pass"


# print(is_valid_pass("Saikat123"))


# --- Checks if email has a basic valid format


def is_valid_email(email):
    return "@" in email and "." in email


# email = is_valid_email("Saikatgharami2@gmail.com")
# print(email)


def process_user_email(email):
    write_log("App started")
    # --- Receive an email from the user
    # --- Check if it is valid or not
    # --- If not valid, log the problem
    if not is_valid_email(email):
        write_log(f"Invalid email received : {email}")
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email : {clean_email}")
    write_log("App stopped")


email = input("Enter email : ")
process_user_email(email)

# --- Done --- #
