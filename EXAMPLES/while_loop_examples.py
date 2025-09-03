print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    try:
        quantity = int(raw_quantity)  # could validate via try/except
    except ValueError as err:
        print("invalid number")
        continue
    else:
        print(f"sending {quantity} ticket(s)")
