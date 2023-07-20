#Day 5: Final project: - Password Generator

import random
import string
print("Welcome to Password Generator.com")
letter=string.ascii_letters
numbers=string.digits
symbols=string.punctuation
l=int(input("How many letters do you wanted in your Password?\n"))
result_str = ''.join(random.choice(letter) for item in range(l))
n=int(input("How many Numbers do you wanted in your Password?\n"))
result_num = ''.join(random.choice(numbers) for num in range(n))
s=int(input("How many Symbols do you wanted in your Password?\n"))
result_pun = ''.join(random.choice(symbols) for sym in range(s))
fin=''
result= result_str+result_num+result_pun
w=len(result)
for pwd in range(w):
    fin+= ''.join(random.choice(result))
print(f"Your New Password Generated is:\n{fin}")
