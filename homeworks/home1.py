rice_price = 45       
sugar_price = 40      
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

ricetot = rice_price * rice_qty
sugartot = sugar_price * sugar_qty
oiltot = oil_price * oil_qty

print("Total price for rice", ricetot)
print("Total price for sugar", sugartot)
print("Total price for oil", oiltot)


finalbill = ricetot + sugartot + oiltot
print("Final bill amount:", finalbill)

finalbill_int = int(finalbill)
print("Final bill amount (as integer):", finalbill_int)

finalbill_str = str(finalbill)
print("Final bill amount (as string):", finalbill_str)

import random
delivery_charge = random.randint(5, 10)
final_bill = finalbill + delivery_charge
print("Delivery charge is", delivery_charge)
print("Final bill is",final_bill)