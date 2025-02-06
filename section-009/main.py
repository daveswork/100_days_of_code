import art

print(art.logo)

bids = {}

def get_bid() -> None:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

keep_bidding = True

while keep_bidding:
    get_bid()
    keep_going = input("Are there any other bidders? Type 'yes or 'no'.")
    if keep_going == "no":
        keep_bidding = False
    else:
        print("\n" * 20)

winning_bidder = {"winner": {"name":"", "bid":0}}

for bidder in bids:
    if bids[bidder] > winning_bidder["winner"]["bid"]:
        winning_bidder["winner"]["name"] = bidder
        winning_bidder["winner"]["bid"] = bids[bidder]
print(f'The winner is {winning_bidder["winner"]["name"]} with a bid of ${winning_bidder["winner"]["bid"]}')


