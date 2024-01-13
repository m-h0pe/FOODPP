from Menu_2 import MenuBrowsingModule
from Order_2 import OrderPaymentModule

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
order_payment_module = OrderPaymentModule(menu_browser)

# Display the menu
menu_browser.display_menu()

# Add items to the cart
menu_browser.add_to_cart('Italian', 'Margherita Pizza', 2)
menu_browser.add_to_cart('Mexican', 'Tacos', 3)

# Place an order with payment
order_payment_module.place_order()
