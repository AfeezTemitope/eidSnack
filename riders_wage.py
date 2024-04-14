result = []
continue_input = "Y"

while continue_input.lower() == "y":
    successful_deliveries = int(input("Enter number of successful deliveries:"))
    base_pay = 5000

    if successful_deliveries < 50:
        amount_per_parcel = 160
    elif 50 <= successful_deliveries <= 59:
        amount_per_parcel = 200
    elif 60 <= successful_deliveries <= 69:
        amount_per_parcel = 250
    else:
        amount_per_parcel = 500

    riders_payment = successful_deliveries * amount_per_parcel + base_pay
    test_result = "Test Result (Successful)" if successful_deliveries >= 100 else "Test Result (Failed)"
    result.append(f"Delivery {successful_deliveries} {test_result} : {riders_payment}")

    continue_input = input("Do you want to enter more deliveries? (y/n)")

for res in result:
    print(res)
