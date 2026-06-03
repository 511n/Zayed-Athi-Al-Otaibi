amount_due = 50

while amount_due > 0:
    coin = input("Insert Coin: ")

    try:
        coin = int(coin)
    except ValueError:
        print("Please insert a valid integer coin")
        continue

    if coin not in [5, 10, 25]:
        print(f"Coin not accepted. Returning {coin} cents")
        print(f"Amount Due: {amount_due}")
        continue

    amount_due -= coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

print(f"Change Owed: {abs(amount_due)}")balance = 1000

while True:
    print("\n1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        while True:
            amount = int(input("Deposit (50,100,200,500) or 0 to cancel: "))

            if amount == 0:
                break
            elif amount in [50, 100, 200, 500]:
                balance += amount
                print("New balance:", balance)
                break
            else:
                print("Invalid amount")

    elif choice == "3":
        while True:
            amount = int(input("Withdraw (50,100,200,500) or 0 to cancel: "))

            if amount == 0:
                break
            elif amount in [50, 100, 200, 500]:
                if amount <= balance:
                    balance -= amount
                    print("New balance:", balance)
                else:
                    print("Insufficient funds")
                break
            else:
                print("Invalid amount")

    elif choice == "0":
        print("Goodbye")
        break

    else:
        print("Invalid choice")inventory = {
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
            )company = {
    "ceo": "Ahmed",
    "departments": {
        "engineering": {
            "manager": "Sara",
            "team_size": 12,
            "projects": ["Backend API", "Mobile App"],
        },
        "design": {
            "manager": "Omar",
            "team_size": 5,
            "projects": ["Website Redesign"],
        },
    },
}

print("CEO:", company["ceo"])
print("Engineering manager:", company["departments"]["engineering"]["manager"])
print("Design team size:", company["departments"]["design"]["team_size"])
print("First engineering project:", company["departments"]["engineering"]["projects"][0])

total_team_size = (
    company["departments"]["engineering"]["team_size"]
    + company["departments"]["design"]["team_size"]
)

print("Total team size:", total_team_size)

company["departments"]["design"]["team_size"] = 6

company["departments"]["marketing"] = {
    "manager": "Lina",
    "team_size": 3,
    "projects": []
}

print("Marketing:", company["departments"]["marketing"])student = {
    "name": "Ali",
    "age": 17,
    "grade": "11"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])prices = {"apple": 3, "banana": 2}

prices["mango"] = 5
prices["apple"] = 4

print(prices)user = {
    "name": "Sara",
    "email": "sara@example.com",
    "city": "Jeddah"
}

print("Keys:", list(user.keys()))
print("'name' in dict:", "name" in user)
print("'phone' in dict:", "phone" in user)nums = [10, 20, 30, 40, 50]

print("Count:", len(nums))
print("Sum:", sum(nums))
print("First:", nums[0])
print("Last:", nums[-1])shopping = ["bread", "milk", "eggs"]

shopping.append("cheese")
shopping.remove("milk")

print(shopping)colors = {"red", "blue", "green"}

colors.add("yellow")
colors.add("red")

print("Size:", len(colors))
print("red in set:", "red" in colors)
print("yellow in set:", "yellow" in colors)nums = [1, 2, 2, 3, 4, 4, 5, 1]

unique_nums = set(nums)

print("Unique values:", unique_nums)
print("Count of unique values:", len(unique_nums))a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("In a but not in b:", a - b)person = ("Sara", 25, "Riyadh")

print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])colors = ("red", "green", "blue")



print("Length:", len(colors))
print("red in tuple:", "red" in colors)