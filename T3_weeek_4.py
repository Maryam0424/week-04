items = {
    "A001": {"description": "Antique vase", "current_highest_bid": 500, "reserve_price": 1000, "num_bids": 3},
    "B002": {"description": "Vintage painting", "current_highest_bid": 800, "reserve_price": 1200, "num_bids": 5},
    "C003": {"description": "Rare collectible coin", "current_highest_bid": 300, "reserve_price": 500, "num_bids": 1},
    }

def end_auction():
    total_fee = 0
    items_sold = 0
    items_below_reserve = 0
    items_no_bids = 0

    print("Items sold: ")
    for item_number, item_details in items.items():
        final_bid = item_details['current_highest_bid']
        reserve_price = item_details['reserve_price']
        num_bids = item_details['num_bids']

        if final_bid >= reserve_price:
            items_sold += 1
            auction_fee = 0.1 * final_bid
            total_fee += auction_fee
            print(f"Item Number: {item_number}, final Bid: {final_bid}, Auction Fee: {auction_fee}")

        elif num_bids > 0:
            items_below_reserve += 1
            print(f"Item Number: {item_number}, Final Bid: {final_bid} (Below Reserve Price)")
        
        else:
            items_no_bids += 1
            print(f"Item Number: {item_number} (No Bids)")

    print(f"\nTotal Auction Company Fee for Sold Items: {total_fee}")
    print(f"Number of Items Sold: {items_sold}")
    print(f"Number of Items Below Reserve Price: {items_below_reserve}")
    print(f"Number of Items with No Bids: {items_no_bids}")

end_auction()