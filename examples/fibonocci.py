 n = int(input('enter the number:'))
i =0
a = 0
series =0
fibn=[]

while n > 0:
    fibn.append(series)
    i = i + 1
    a = series
    series = series + a 
    n = n - 1   
print(fibn)
  
   