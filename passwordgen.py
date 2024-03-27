import random
import time

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%^&*()-_+=|][{}/?<>.,"

all = lower+upper+numbers+symbols
length = 16
password = "".join(random.sample(all,length))
usrinput = input("Hello, would you like to generate a password?: [yes/no]:\n")
usrinput = usrinput.lower()
if usrinput == "yes":
    time.sleep(1)
    print(f"Here is a generated password: {password}.")
else:
    input("password: ")
    time.sleep(1)
    print("Password Saved!")