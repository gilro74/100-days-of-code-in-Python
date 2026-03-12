print("Welcome to the Secret Auction Program")
auction ={}
name = input("What is your name?: ")
bid_number = int(input("What is your bid?: $"))
auction[name] =bid_number
other_bidders = input('''Are they other bidders? Type 'yes' or 'no': \n''').lower()


while other_bidders =="yes":
    print("\n"*100)
    name = input("What is your name?: ")
    bid_number = input("What is your bid?: $")
    auction[name] =bid_number
    other_bidders = input('''Are they other bidders? Type 'yes' or 'no': \n''').lower()




def find_highest_bidder(bidding_dictionery):
    winner = ""
    highest_bid = 0

    max(bidding_dictionery)
    for i in bidding_dictionery:
        bid_amount = int(bidding_dictionery[i])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i


    print(f" The winner is {winner} with bidding amount of ${auction[winner]}")



print(find_highest_bidder(auction))
# count = 0
# for i in auction:
   
#     score = int(auction[i])
#     if score > count:
#         print(f"{i} wins")
#     count = score
#     print(score)
# print(auction)


