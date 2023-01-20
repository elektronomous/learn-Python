from logo import logo
from os import system

def main():
    print(logo);

    auction = True;
    bidder = {}

    while auction:
        name = input("What's your name?: ");
        bid = float(input("What's your bid?: $"));

        # add the name and his/her bid to dictionary
        bidder[name] = bid;

        anyBidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower();

        if anyBidder == 'no':
            auction = False;
        system('clear');
    

    highestBid = 0;
    winnerName = '';
    for name in bidder:
        if highestBid < bidder[name]:
            winnerName = name;
            highestBid = bidder[name];
    
    print(f"The winner is {winnerName} with a bid of ${int(highestBid)}.");

if __name__ == "__main__":
    main();

