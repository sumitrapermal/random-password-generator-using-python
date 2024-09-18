#create a Alphabet (A-Z) password
#Python has a built-in module that you can use to make random numbers.

import random
password="abcdefghijklmnopqrstvuwxyz"
length=int(input("Enter the length of the password : "))

#join() method takes all items in an iterable and joins them into one string.
#The sample() method returns a value with a specified number of randomly selected items from a sequence

a="".join(random.sample(password,length))
print(f"the password is : {a}")
