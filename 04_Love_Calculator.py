name1 = input("Please enter your name: ")
name2 = input("Please enter your partner's name: ")

name_combo = name1 + name2

name_combo = name_combo.lower()
print(name_combo)

love_check1 = 'true'

love_check2 = 'love'

check1 = 0
for i in love_check1:
    # print(i)
    check1 += name_combo.count(i)

check2 = 0
for i in love_check2:
    check2 += name_combo.count(i)

# print(check1, check2)

result = str(check1) + str(check2)
# print(type(result))
result = int(result)
# print(type(result))
# print(result)

if (result < 10 or result > 90):
    print(f"Your score is {result}%, you go together like coke and mentos!")
elif (result >= 40 and result <= 50):
    print(f"Your score is {result}%, you are alright together")
else:
    print(f"Your score is {result}%")
