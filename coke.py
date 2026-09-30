def main():
    amount_due = 50
    coins = [5, 10, 25]

    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))

        if coin in coins:
            amount_due = amount_due - coin

    print("Payment complete! Take your Coke.")


main()
