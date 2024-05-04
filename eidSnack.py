from datetime import datetime

customer_name = input("Customer name: ")
cashier_name = input("Cashier name: ")
date = datetime.now

bad_afeez = []

    
user_item = input("What did you want to buy? ")
quantity = float(input("How many pieces: "))
price_of_one_item = float(input("How much per unit: "))
total = quantity * price_of_one_item
bad_afeez.append((user_item, quantity, price_of_one_item, total))

continue_shopping = input("Do you want to buy something else? (yes/no): ")
if continue_shopping.lower() != "yes":
            break

discount_percentage = float(input("Enter discount percentage: "))
discount = total * (discount_percentage / 100)

vat_percentage = 17.50 / 100
vat = vat_percentage * total
bill_total = (total - discount) + vat

print("")
print("SEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 03293828343")
print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {customer_name}\t")
print(f"DATE: {date}\n")
print("==========================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")

for item, qty, price, item_total in bad_afeez:
        print(f"{item}\t{qty}\t{price}\t{item_total:.2f}")

print("-------------------------------------------")
print(f"Sub-Total: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT @ 17.50%: {vat:.2f}\n")
print("==========================================\n")
print(f"Bill Total: {bill_total:.2f}\n")
print("==========================================\n")
print(f"THIS IS NOT A RECEIPT. KINDLY PAY {bill_total:.2f}\n")
print("==========================================\n")

paid = float(input("How much did the customer give you?: "))
print("")
print("SEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 03293828343")
print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {customer_name}\t")
print(f"DATE: {date}\n")
print("==========================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")

for item, qty, price, item_total in bad_afeez:
        print(f"{item}\t{qty}\t{price}\t{item_total:.2f}")

print("-------------------------------------------")
print(f"Sub-Total: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT @ 17.50%: {vat:.2f}\n")
print("==========================================\n")
print(f"Bill Total: {bill_total:.2f}")
print(f"Amount Paid: {paid:.2f}")
print(f"Balance: {paid - bill_total:.2f}\n")
print("==========================================\n")
print("\nTHANK YOU FOR YOUR PATRONAGE")