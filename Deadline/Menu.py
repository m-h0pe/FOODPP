class MenuBrowsingModule:
    def __init__(self, menu):
        self.menu = menu
        self.cart = {}

    def display_menu(self):
        print("Menu:")
        for cuisine, items in self.menu.items():
            print(f"\n{cuisine} Cuisine:")
            for item in items:
                print(f"{item['name']} - ${item['price']}")

    def add_to_cart(self, cuisine, item_name, quantity):
        if cuisine in self.menu and any(item['name'] == item_name for item in self.menu[cuisine]):
            item = next(item for item in self.menu[cuisine] if item['name'] == item_name)
            if item_name in self.cart:
                self.cart[item_name]['quantity'] += quantity
            else:
                self.cart[item_name] = {'quantity': quantity, 'price': item['price']}
            print(f"{quantity} {item_name}(s) added to the cart.")
        else:
            print("Item not found in the menu.")

    def view_cart(self):
        print("\nShopping Cart:")
        for item, details in self.cart.items():
            print(f"{item} - Quantity: {details['quantity']} - Total: ${details['quantity'] * details['price']}")

# Example Usage:
menu_data = {
    'Italian': [
        {'name': 'Margherita Pizza', 'price': 12.99},
        {'name': 'Spaghetti Bolognese', 'price': 15.99},
    ],
    'Mexican': [
        {'name': 'Tacos', 'price': 8.99},
        {'name': 'Burrito', 'price': 10.99},
    ],
    # Add more cuisines and items as needed
}

menu_browser = MenuBrowsingModule(menu_data)

# Display the menu
menu_browser.display_menu()

# Add items to the cart
menu_browser.add_to_cart('Italian', 'Margherita Pizza', 2)
menu_browser.add_to_cart('Mexican', 'Tacos', 3)

# View the shopping cart
menu_browser.view_cart()
