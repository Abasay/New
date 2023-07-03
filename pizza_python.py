print('Welcome to Python Pizza Deliveries')
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want  extra cheese? Y or N ")


if (size == "S"):
    pizza_price = 15
    if (add_pepperoni == "Y"):
        pepperoni_price = 2
    else:
        pepperoni_price = 0
elif (size == "M"):
    pizza_price = 20
    if (add_pepperoni == "Y"):
        pepperoni_price = 3
    else:
        pepperoni_price = 0
elif (size == "L"):
    pizza_price = 25
    if (add_pepperoni == "Y"):
        pepperoni_price = 3
    else:
        pepperoni_price = 0
else:
    print("Oops, Error input!!!")

if (extra_cheese == "Y"):
    extra = 1
else:
    extra = 0

bill = pizza_price + pepperoni_price + extra


print("Your final bill is: ${}.".format(bill))
