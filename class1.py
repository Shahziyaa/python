applejuice = 15.5
orangejuice = 20
grapejuice = 10.25  

totalvol = applejuice + orangejuice + grapejuice
print("Total volume of juice:", totalvol)

totalvol_int= int(totalvol)
print("Total volume of juice (as integer):", totalvol_int)

totalvol_str = str(totalvol)
print("total volume of juice as string",totalvol_str)


import random
bonus = random.randint(5,10)
final_tot = totalvol + bonus
print("Final total volume of juice after bonus:", final_tot)