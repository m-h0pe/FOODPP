class OrderModule:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, item_name, quantity, price):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'quantity': quantity, 'price': price}

    def confirm_order(self):
        if not self.cart:
            print("Your cart is empty. Add items before confirming the order.")
            return

        total_price = sum(item['quantity'] * item['price'] for item in self.cart.values())
        print("\nOrder Summary:")
        for item, details in self.cart.items():
            print(f"{item} - Quantity: {details['quantity']} - Total: ${details['quantity'] * details['price']}")
        print(f"\nTotal Price: ${total_price}")

        # Here, you might integrate with a payment gateway for the actual transaction.

        print("Order confirmed! Thank you for your purchase.")
        self.cart = {}  # Clear the cart after confirming the order

# Example Usage:
order_module = OrderModule()

# Add items to the cart
order_module.add_to_cart('Pizza', 2, 12.99)
order_module.add_to_cart('Burger', 3, 8.99)

# Confirm the order
order_module.confirm_order()
