# Initialize an empty dictionary to store the auction bids
auction_data = {}

# Welcome message
print("Welcome to the secret auction program")

while True:
    # Get the name and bid amount from the user
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # Store the bid in the dictionary with the name as the key
    auction_data[name] = bid

    # Ask if there are any other bidders
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
 
    if more_bidders == "no":
        break
  

# Find the highest bidder



highest_bidder = max(auction_data, key=auction_data.get)
print(highest_bidder)
highest_bid = auction_data[highest_bidder]

# Announce the winner
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
