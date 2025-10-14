head = """book store
receipt"""
print(head.upper())

item1 = "python basics"
price1 = 450
item2 = "data science intro"
price2 = 600

print(item1.upper(), '->',price1)

print(item2.upper(),'->' price2)
message = f"customer1 bought {item1} for {price1} and {item2} for {price2}."
print(message.upper())

totalprice = price1 + price2
print("Total price is:\t".upper(), totalprice)

string1 = "thankyou"
string2 = "for shopping"
end = string1 + " " + string2
print(end.upper())