food_item = input("Enter food item name:\n")
item_price = float(input("Enter item price:\n"))
item_quantity = int(input("Enter item quantity:\n"))

print()

print("RECEIPT")
print(
    f"{item_quantity} {food_item} @ ${item_price:.2f} = \
${item_quantity * item_price:.2f}"
)


print(f"Total cost: ${item_quantity * item_price:.2f}")

print()
print()

food_item2 = input("Enter second food item name:\n")
item_price2 = float(input("Enter item price:\n"))
item_quantity2 = int(input("Enter item quantity:\n"))

print()

print("RECEIPT")
print(
    f"{item_quantity} {food_item} @ ${item_price:.2f} = \
${item_quantity * item_price:.2f}"
)
print(
    f"{item_quantity2} {food_item2} @ ${item_price2:.2f} = \
${item_quantity2 * item_price2:.2f}"
)
print(
    f"Total cost: \
 f${(item_quantity * item_price) + (item_quantity2 * item_price2):.2f}"
)

print()

total_cost = ((item_quantity * item_price) + (item_quantity2 * item_price2)) * 0.15

print(f"15% gratuity: ${total_cost:.2f}")
print(
    f"Total with tip: \
${((item_quantity * item_price) + (item_quantity2 * item_price2)) + total_cost:.2f}"
)
# print('hello world')
