import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num = len(names)
print(names[0])
random_int = random.randint(0,num-1)
print(f"{names[random_int]} is going to buy the meal")


# Dirty_Dozen
fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "celery"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)