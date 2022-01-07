import math
import re


special_characters = "!@#$%^&*()-+?_=,<>/"

print('----------------------------')
print('How Secure is Your Password?')
print('----------------------------')
password = input('Enter a password : ')
length_password = len(password)
number_characters = 0

upper = "NO"
lower = "NO"
symbol = "NO"
number = "NO"

if re.search('[a-zA-Z]', password):
    if password.isupper():
        number_characters += 26
        upper = "YES"
    elif password.islower():
        number_characters += 26
        lower = "YES"
    else:
        number_characters += 52
        upper = "YES"
        lower = "YES"
if any(c in special_characters for c in password):
    number_characters += 32
    symbol = "YES"

if any(map(str.isdigit, password)):
    number_characters += 10
    number = "YES"

print('----------------------------')
print("{} characters containing".format(length_password))
print("Upper case : {}".format(upper))
print("Lower case : {}".format(lower))
print("Numbers : {}".format(number))
print("Symbols : {}".format(symbol))
print('----------------------------')

"""
In the calculation examples, 
a generation of 2 billion keys per second is expected, 
since this corresponds approximately to the speed of a very strong single computer.
ref.https://www.password-depot.de/en/know-how/brute-force-attacks.htm
"""
# Possible combinations = possible number of characters ** Password length
time_decrypt = ((number_characters ** length_password) / 2000000000)
if time_decrypt < 60:
    print("Time to crack password : {:.2f} seconds".format(time_decrypt))
    print("Very Weak Password")
# minutes = seconds ÷ 60
elif 60 <= time_decrypt < 86400:
    print("Time to crack password : {} minutes".format(math.ceil(time_decrypt/60)))
    print("Weak Password")
# days = seconds ÷ 86,400
elif 86400 <= time_decrypt < 31556952:
    print("Time to crack password : {} days".format(math.ceil(time_decrypt/86400)))
    print("Medium Password")
# years = seconds ÷ 31,556,952
else:
    print("Time to crack password : {} years".format(math.ceil(time_decrypt/31556952)))
    print("Strong Password")
