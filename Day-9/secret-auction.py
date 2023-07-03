from os import system

#system('cls')

print("Welcome to the secret auction program.\n")
bid_infos = {}
other_bidders= True
def auction():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_infos[name] = bid

while other_bidders:
    auction()
    bidders_input = input("Are there other bidders?. Type 'yes' or 'no': ")
    if bidders_input == 'yes':
        other_bidders = True
    else:
        other_bidders = False
        continue
    system('cls')

max_bid = 0
winner_bidder = ""
for key in bid_infos:
    if max_bid < bid_infos[key]:
        max_bid = bid_infos[key]
        winner_bidder = key
print(f"The person with the highest bid is {winner_bidder} with a bid of ${max_bid}")
