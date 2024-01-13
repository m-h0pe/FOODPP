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

    def get_cart_total(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())
