menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cost = 0
while True:
    try:
        order = input("Place your order enter control -d to finish your order")
        order.title()
        cost = cost + menu[order]
        print(order, f": ${menu[order]}")
        print(f"Total cost: $", cost)
    except EOFError:
        print("Thank you for ordering with us")
        break
