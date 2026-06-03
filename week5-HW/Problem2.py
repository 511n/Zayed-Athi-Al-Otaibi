inventory = {
    "laptop": 5,
    "mouse": 10,
    "keyboard": 0
}

orders = [
    ("laptop", 2),
    ("mouse", 15),
    ("keyboard", 1),
    ("monitor", 3),
]

for product, qty in orders:
    match product:
        case _ if product not in inventory:
            print(f"{product}: not in inventory")

        case _ if inventory[product] >= qty:
            inventory[product] -= qty
            print(f"{product}: shipped {qty}, {inventory[product]} left")

        case _:
            print(
                f"{product}: only {inventory[product]} in stock, cannot ship {qty}"
            )