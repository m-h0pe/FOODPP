class MenuBrowsingModule:
    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
        print("Menu:")
        for cuisine, items in self.menu.items():
            print(f"\n{cuisine} Cuisine:")
            for item in items:
                print(f"{item['name']} - ${item['price']}")

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

