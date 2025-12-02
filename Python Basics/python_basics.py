# --------------------------------------------
# Topic 1: Python Basics - Generative AI B.Tech Core
# --------------------------------------------

# Variables
x = 10
print(x)

mysub = "python"
print(mysub)

_mycity = "Solan"
print(_mycity)

my_sub1 = "Generative AI"
print(my_sub1)

import keyword
print(keyword.kwlist)

# Data Types
x = 0
print(type(x))

y = 1.0
print(type(y))

z = 3 + 4j
print(type(z))

a = "solan"
print(type(a))

a = True
print(type(a))

e = None
print(type(e))

# String
my_sub = 'Generative AI'
print(type(my_sub))

my_college = "Shoolini University"
print(type(my_college))

my_sentence = '''This sentence is multiple lines,
this is also a string'''
print(type(my_sentence))

# String length and indexing
my_sub = "Machine learning"
print(len(my_sub))
print(my_sub[0])
print(my_sub[-1])
print(my_sub[4])

# Slicing
print(my_sub[0:7:1])

# Concatenation
first_name = "Amit"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(full_name)

# String methods
print(my_sub.lower())
print(my_sub.upper())
print(my_sub.count("a"))

# -----------------------------
# Lists
# -----------------------------
my_list = [98, 34, 56, "apple", True]
print(my_list)
print(type(my_list))

my_list = [10, 4, 5, 6, 7]
list1 = ["apple", True, 2, 3.14, None]

# Indexing
my_list = [23, 45, 98, 12, 56]
print(my_list[0])
print(len(my_list))
print(my_list[-1])

# Slicing
my_list = [2, 4, 7, 8, 9, 5, 3]
print(my_list[0:6])
print(my_list[::-1])
print(my_list[:])

# Concatenation
list1 = [3, 4, 5, 6]
list2 = [6, 7, 8, 9]
print(list1 + list2)

# List functions
my_list = [1, 2, 3, 4, 5, 6]
print(min(my_list))
print(max(my_list))
print(sum(my_list))

list1 = [8, 6, 9, 3, 10, 5, 2]
print(sorted(list1))
print(sorted(list1, reverse=True))

my_list.append(100)
print(my_list)

list1.extend([90, 89, 76])
print(list1)

# Pop & Remove
my_list = [78, 45, 35, 78, 90]
print(my_list.pop())
print(my_list)
print(my_list.pop(2))
print(my_list)

list1 = [67, 89, 45, 34]
list1.remove(89)
print(list1)

# -----------------------------
# Dictionary
# -----------------------------
my_dict = {"Name": "Kritika", "College": "Shoolini"}
print(type(my_dict))
print(my_dict)

print(my_dict["Name"])
print(my_dict["College"])

print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))
print(my_dict.get("Name"))
print(my_dict.get("Age", "Age is not present"))

my_dict.update({"Age": 20})
print(my_dict)
my_dict.update({"Name": "Jagat"})
print(my_dict)

# -----------------------------
# Conditional Statements
# -----------------------------
age = 25
if age > 60:
    print("You are too old for marriage")
elif age < 18:
    print("You are too young for marriage")
else:
    print("We will find a perfect match for you")

# -----------------------------
# Loops
# -----------------------------
my_sub = "python"
for i in my_sub:
    print(i)

for i in range(len(my_sub)):
    print(my_sub[i], "->", i)

my_list = [89, 76, 45, 34]
for i in my_list:
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

# Break
i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)

# Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Pass
i = 0
while i < 5:
    i += 1
    if i == 3:
        pass
    print(i)

# -----------------------------
# Functions
# -----------------------------
def Calculation(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

Calculation(10, 5)

# Default Argument
def area_perimeter(width=8, height=4):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

print(area_perimeter(10, 8))

# Keyword Argument
def interest(p, r, t):
    i = (p * r * t) / 100
    return i

print(interest(t=2, p=1000, r=10))

# Variable length args
def sum_number(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_number(4, 5, 6, 7))

def test(**kwargs):
    print(kwargs)

test(a=10, b=20, c=30)
