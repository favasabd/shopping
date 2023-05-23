products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}
discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.1),
    "tiered_50_discount": (30, 0.5)
}

gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10


def calculate_product_total(quantity, price, is_gift_wrapped):
    product_total = quantity * price

    if is_gift_wrapped:
        product_total += quantity * gift_wrap_fee

    return product_total


def calculate_applicable_discount(total_quantity):
    applicable_discount = 0

    for rule, (threshold, discount) in discount_rules.items():
        if total_quantity > threshold and discount > applicable_discount:
            applicable_discount = discount

    return applicable_discount


def calculate_shipping_fee(total_quantity):
    packages = (total_quantity - 1) // units_per_package + 1
    shipping_fee = packages * shipping_fee_per_package

    return shipping_fee


def input_order_details():
    order_details = {}

    for product, price in products.items():
        quantity = int(input(f"Enter the quantity of {product}: "))
        is_gift_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"

        product_total = calculate_product_total(quantity, price, is_gift_wrapped)
        order_details[product] = (quantity, product_total)

    return order_details


def calculate_order_totals(order_details):
    subtotal = 0
    total_quantity = 0

    for _, (quantity, product_total) in order_details.items():
        subtotal += product_total
        total_quantity += quantity

    discount_amount = calculate_applicable_discount(total_quantity)
    shipping_fee = calculate_shipping_fee(total_quantity)

    total = subtotal - discount_amount + shipping_fee

    return subtotal, discount_amount, shipping_fee, total


def main():
    order_details = input_order_details()
    subtotal, discount_amount, shipping_fee, total = calculate_order_totals(order_details)

    print("\nOrder Details:")
    for product, (quantity, product_total) in order_details.items():
        print(f"Product: {product}")
        print(f"Quantity: {quantity}")
        print(f"Total: ${product_total}")
        print()

    print("Order Summary:")
    print(f"Subtotal: ${subtotal}")
    if discount_amount > 0:
        print(f"Discount Applied: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Total: ${total}")


main()
