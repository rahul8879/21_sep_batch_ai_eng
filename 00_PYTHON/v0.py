# variables ??
# c/java
# age = "24.6"
# print(type(age))

# age_@_2 = 34
# print(age_@_2)


# if = 4
# print(and)

# import keyword
# print(keyword.kwlist)

# Variable declartion rules
    # 1. Variable names can only contain letters, numbers, and underscores.
    # 2. Variable names must start with a letter or underscore.
    # 3. Variable names cannot be a keyword.

# Types of variables( data type)
# int
# float
# str
# bool
# list
# tuple
# dict
# set
# frozenset

# operations
# arithmetic operators
# +, -, *, /, //, %, **

# comparison operators
# ==, !=, >, <, >=, <=

# logical operators
# and, or, not

# x = 23.5
# y ="34.5"
# # print(x + y)
# print(float(y)) 

# Above code snippet is an example of type casting 

# flag = True
# if flag:
#     if 4 < 3:
#         print("4 is less than 3")
#     elif 4 > 3:
#         print("4 is greater than 3")
#     else:
#         print("4 is equal to 3")
#     print("flag is true")
#     print("This is a nested block")
#     print("This is a nested block")
# #print("This is outside the block")
# elif 6 > 9:
#     if 6 < 9:
#         print("6 is less than 9")
#     else:
#         print("6 is greater than 9")

# ssn_no = input("Enter your SSN number: ")
# # print(type(ssn_no))
# # print(len(ssn_no))
# if (len(ssn_no) == 9) and (ssn_no.isdigit()):
#     print("Valid SSN number")

# 100 days sales records ?? store them --> simple singular variable --> int or float ??
# data structure --> list, tuple, dict
sales = [45.89, 56.78, 67.89, 78.90, 89.01, 90.12, 12.34, 23.45, 34.56, 45.67]

# accessing elements
# print(sales[0:6]) # syntax for slicing lst[start:end]
# print(sales[6:])  # syntax for slicing lst[start:end]
# print(sales[:6])  # syntax for slicing lst[start:end]
# print(sales[-1])  # syntax for slicing lst[start:end]

#print(sales[0::3]) # syntax for slicing lst[start:end:step]
sales[1] = 100.00 # updating the value of the list
print(sales)

# operations 
# add 
# remove
# search 

# sales.append(99.99)
# print(sales)

# day_2 = [344.56, 456.78, 567.89, 678.90, 789.01, 890.12, 123.45, 234.56, 345.67, 456.78]
# sales.extend(day_2)
# print(sum(sales))

# https://docs.python.org/3.4/tutorial/datastructures.html

# sales = (45.89, 56.78, 67.89, 78.90, 89.01, 90.12, 12.34, 23.45, 34.56, 45.67)
# sales[1] = 100.00 # updating the value of the tuple

# prompt = "You are a helpful assistant."
# print(len(prompt))

prompt = """
You are a email classification assitant 
Below is my email


Classify into one of the category
- Spam
- Important
- Social
- Promotions
Below is past emails:


"""

emails= [
    "Congratulations! You've won a $1,000 Walmart gift card. Click here to claim your prize.",
    "Important: Your account has been compromised. Please reset your password immediately.",
    "Hey, I saw your post on social media. Let's connect!",
    "Limited time offer: Get 50% off your next purchase!"
]


# def llm(prompt):
#     return "Important"


# for i in emails:
#     updated = prompt + i +j
#     print(updated)
    
