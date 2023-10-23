Silent Auction


from replit import clear
#You can call clear() to clear the output in the console.

#Import logo from art.
from art import logo
print(logo)

print("\n")

#Create appropriate variables and empty dictionary.
bids = {}
bidding_finished = False

#Define a function and nest necessary dictionary.
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #Using a For Loop to run through all the bids within the program.
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        #If condition is used within the program to establish conditions for the highest bid and determining the winner.
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print("\n")
    print(F"The winner is {winner} with a bid of ${highest_bid}.")

#Using a While Loop allows you to continue the program until every bid is input. Using Boolean values allows you to exit the While Loop once all bids have been submitted. 
while not bidding_finished:    
    name = input("What is your name?: \n\n")
    print("\n")
    price = int(input("What is your bid?: \n\n$"))
    print("\n")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No' ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
        #Applying this clear function allows the bidding information to be clear for the following bid.

