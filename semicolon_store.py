import datetime
customer_name = input("Customer name: ")
cashier_name = input("Cashier name: ")
items = []
total = 0
vat_percentage = 17.5 / 100

while True:
    item_name = input("What did you want to buy? ")
    quantity = float(input("How many pieces: "))
    price_per_unit = float(input("How much per unit: "))
    total += quantity * price_per_unit
    items.append((item_name, quantity, price_per_unit, quantity * price_per_unit))
    continue_shopping = input("Do you want to buy something else? (yes/no): ")
    if continue_shopping.lower() != "yes":
        break

discount_percentage = float(input("Enter discount percentage: "))
discount = total * (discount_percentage / 100)
vat = vat_percentage * total
bill_total = (total - discount) + vat

print("\nSEMICOLON  STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 03293828343")
print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {customer_name}")
print(f"DATE: {datetime.datetime.now()}")
print("==========================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")
for item in items:
    print(f"\t{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
print("-------------------------------------------")
print(f"Sub-Total: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT @ 17.50% : {vat:.2f}")
print("\n==========================================\n")
print(f"Bill Total: {bill_total:.2f}")
print("\n==========================================\n")
print(f"THIS IS NOT A RECEIPT KINDLY PAY {bill_total:.2f}")
print("\n==========================================\n")

paid = float(input("How much did the customer gave to you?: "))
balance = paid - bill_total


print("SEMICOLON  STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 03293828343")
print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {customer_name}")
print(f"DATE: {datetime.datetime.now()}")
print("==========================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")
for item in items:
    print(f"\t{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
print("-------------------------------------------")
print(f"Sub-Total: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT @ 17.50% : {vat:.2f}")
print("\n==========================================\n")
print(f"Bill Total: {bill_total:.2f}")
print(f"Amount Paid: {paid:.2f}")
print(f"Balance: {balance:.2f}")
print("\n==========================================\n")
print("\n THANK YOU FOR YOUR PATRONAGE ")

