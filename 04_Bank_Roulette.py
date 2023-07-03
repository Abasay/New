import random
names = input("Give me the names separated by commas: ")

names_array = names.split(",")

print(names_array)

length = len(names_array)

rand_value = random.randint(0, length)


print(names_array[rand_value])
