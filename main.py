# char_num = len(input("What is your name?\n"))
# print(f'your name has {char_num} characters.')
# print("Welcome to the zoo!")
# height = int(input("what is your height?"))
# print("height: ", height)
# if (height >= 160):
#   print("Welcome to the Zoo")
#   age = int(input("What is your age?"))
#   print("age: ", age)
#   if (age <= 18):
#     print("Please pay $5")
#   else:
#     print("Please pay $10")
# else:
#   print(f"You are not allowed because your height is less than {height}cm")

# print("Welcome to the zoo!")
# height = int(input("what is your height?"))
# age = int(input("What is your age?"))
# price = "$10" if age >= 18 else "$5"
# # if (height > 160 & age > 18):
# #   print("Please pay $10")
# # elif (height > 160 & age < 18):
# #   print("Please pay $5")
# # else:
# #   print(f"Your height {height} is not enough to enter the zoo")
# result = "GooLuck" if height >= 160 and age >= 18 else "Noluck"
# print(result)
# print(f"Price to enter the park is {price}")

# print('Welcome to the Zoo!')
# height = int(input("what is your height?"))
# if height >= 170:
#   print("You are authorised to enter")
#   age = int(input("What is your age?"))
#   price = 10 if age >= 18 else 5
#   str(input("Do you wanna photo? Y / N\n"))
#   if "Y":
#     price += 3
#   print(f"Your total price is {price}")
# else:
#   print("Your height is too less to enter")

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? "S", "M", or "L"
# add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
# extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# # Your code below this line 👇
# bill = 0
# bill += 15 if size == "S" else (20 if size == "M" else 25)

# bill += 2 if add_pepperoni == "Y" and size == "S" else (
#     3 if add_pepperoni == "Y" else 0)
# bill += 1 if extra_cheese == "Y" else 0
# print(f"Your final bill is: ${bill}")

import random

random_num = random.randint(1, 10)
print(random_num)
