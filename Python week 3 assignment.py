def calclulate_discount(price, discount_percent):
#check if dicsount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price

    else:
        
        return price

#To prompt user to input original price and discount percentage
price = float(input("Enter original price of item:"))
discount_percent = float(input("Enter discount percentage of item:"))

#calculate the final price of an item using function
final_price = calclulate_discount(price, discount_percent)

#print the final price or the original price
print(f"The final price is: ${final_price:.2f}")

