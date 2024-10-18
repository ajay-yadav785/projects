menu = {
    "noodles": 120,
    "rice": 50,
    "soup": 300,
    "dosa": 100,
    "pizza": 400,
    "paneer_chilli": 300
}

def display_menu():
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price:.2f}")

def take_order():
    order = {}
    while True:
        display_menu()
        item = input("\nEnter the item you want to order (or 'done' to finish): ").lower()
        if item == 'done':
            break
        if item in menu:
            quantity = int(input(f"Enter the quantity for {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not found in menu. Please try again.")
    return order

def calculate_total(order):
    total = 0
    print("\nYour Order:")
    for item, quantity in order.items():
        price = menu[item] * quantity
        print(f"{item.capitalize()} x{quantity}: ${price:.2f}")
        total += price
    print(f"\nTotal Bill: ${total:.2f}")

def main():
    order = take_order()
    if order:
        calculate_total(order)
    else:
        print("No items ordered.")

if __name__ == "__main__":
    main()
