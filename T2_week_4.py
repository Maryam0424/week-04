items = {"A001": {"description": "Antique vase", "current_highest_bid": 0, "num_bids": 0},
    "B002": {"description": "Vintage painting", "current_highest_bid": 0, "num_bids": 0},}

def view_items():
    print("Items available for bidding: ")
    for item_number, item_details in items.items():
        print(f"Item Number: {item_number}")
        print(F"Description: {item_details['description']}")
        print(f"Current Highest Bid: {item_details['current_highest_bid']}")
        print("")

def place_bid(buyer_number):
    item_number = input("Enter the item number you want to bid on: ")
    if item_number not in items:
        print("Invalid item number.")
        return
    current_highest_bid = items[item_number]['current_highest_bid']
    new_bid = float(input(f"Enter your bid (current highest bid: {current_highest_bid}): "))

    if new_bid <= current_highest_bid:
        print("Your bid must be higher than the current highest bid.")
    else:
        items[item_number]['current_highest_bid'] = new_bid
        items[item_number]['num_bids'] += 1
        print("Bid successfully placed.")

view_items()
place_bid("12345")