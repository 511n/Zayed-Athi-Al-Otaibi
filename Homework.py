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

print(f"Change Owed: {abs(amount_due)}")