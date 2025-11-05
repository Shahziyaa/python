

import random
import string

def gen_password(length):
    char=string.ascii_letters + string.digits + string.punctuaction + "@"
    password = ''.join(random.choice(char)) for _in range(length)
    return password

length = int(input("enter the length of password:"))

print("the gen pass is",gen_password(length))