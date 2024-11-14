def calculate_discount(price, discount_percent):
 if discount_percent >= 20:
     discount_amount = price * (discount_percent / 100)  # Convert discount percent to a decimal
     final_price = price - discount_amount  # Subtract discount from the original price
     return final_price
 else:
    return price
 
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)
print(f"The final price is: ${final_price:.2f}")

