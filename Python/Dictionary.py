# Food menu dictionary
menu = {
    "pizza": 10.0,
    "cocola": 2.0,
    "Ice Latte": 1.0,
    "french fries": 3.0,
    "cheese burger": 5.0
}
cart = []
total = 0
# Create a case-insensitive dictionary
menu_lowercase = {key.lower(): key for key in menu}

# Display the menu
print("---- Welcome to the food menu ----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------------------")

while True:
    # Ask the user for their order
    order = input(
        "Please enter your order (or type 'done' to finish): ").lower()
    if order == "done":
        break
    elif order in menu_lowercase:
        # Add the order to the cart and update the total
        original_order = menu_lowercase.get(order)
        cart.append(original_order)
        total += menu[original_order]
        print(
            f"Added {original_order} to your cart. Current total: ${total:.2f}")
    else:
        print("Sorry, we don't have that item.")
# Display the final order summary
