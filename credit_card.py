card_number = input('type in  your card number')

if len(card_number)  < 13 or len(card_number) > 16:
	print('Invalid Card Number!')

else:
    if card_number.startswith("4"):
        card_type = "visa"
    elif card_number.startswith("5"):
        card_type = "MasterCard"
    elif card_number.startswith("37"):
        card_type = "American Express"
    elif card_number.startswith("6"):
        card_type = "Discover"
    else:
        card_type = "unknown"

    print(f"card type {card_type}")