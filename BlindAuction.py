# Print(\n * 100) to clear screen.
# Name is key, bid is value
# Figure out who is highest bidder once everyone has entered the bid.
import GavelArt

print(GavelArt.logo)

doneBidding = False
auctionInfo = {}
maxBid = 0
maxBidder = ""

while not doneBidding:
    name = input("What is your name?:  ")
    bidAmt = int(input("What is your bid?  "))

    auctionInfo[name] = bidAmt

    done = input("\nAre there any other bidders?  Type 'yes' or 'no':  ").lower()
    if done == "no":
        doneBidding = True
    else:
        print("\n" * 100)

# print(f"Dictionary:  {auctionInfo}")

for key in auctionInfo:
    if auctionInfo[key] > maxBid:
        maxBidder = key
        maxBid = auctionInfo[key]

print(f"\nThe winner is {maxBidder} with a winning bid of ${maxBid}.")
