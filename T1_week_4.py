def setup_auction():
    items = []
    while True:
        try:
            num_items = int(input("Enter the number of items in the auction (minimum 10): "))
            if num_items < 10:
                print("Error: Minimum 10 items required.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")

    for i in range(1, num_items + 1):
        print(f"\nItem {i}: ")
        item_number = input("Enter item number: ")
        description = input("Enter item description: ")

        while True:
            try:
                reserve_price = float(input("Enter reserve price: "))
                if reserve_price <= 0:
                    print("Error: Reserve price must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid number for reserve price.")

        items.append((item_number, description, reserve_price, 0))
    return items

def test_setup_auction():
    items = setup_auction()
    assert len(items) >= 10
    print("Auction set up successfully.")

    items = setup_auction

test_setup_auction()