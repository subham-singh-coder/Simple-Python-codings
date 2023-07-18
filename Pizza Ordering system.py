bill1=0
print("Welcome to Pizza House!")
size= str(input("Enter Your Pizza Size [s for Small, m for Medium, l for Large]:\n"))
if size=='s' or size=='S':
    bill1=bill1+15
    print(f"The total bill for your {size} size Pizza is ${bill1}")
    pep=str(input("Do you need Pepperoni over your Pizza? [Yes/No]\n"))
    if pep=='Y' or pep=='y':
        bill1=bill1+2
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    else:
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    che=str(input("DO you need extra cheese over your Pizza? [Yes/No]\n"))
    if che=='y' or che=='Y':
        bill1=bill1+1
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    else:
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    print("Thank You for Visiting Pizza House!")
elif size=='m' or size=='M':
    bill1 = bill1 + 20
    print(f"The total bill for your {size} size Pizza is ${bill1}")
    pep=str(input("Do you need Pepperoni over your Pizza? [Yes/No]\n"))
    if pep=='Y' or pep=='y':
        bill1=bill1+3
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    else:
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    che=str(input("DO you need extra cheese over your Pizza? [Yes/No]\n"))
    if che=='y' or che=='Y':
        bill1=bill1+1
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    else:
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    print("Thank You for Visiting Pizza House!")
elif size=='l' or size=='L':
    bill1 = bill1 + 25
    print(f"The total bill for your {size} size Pizza is ${bill1}")
    pep = str(input("Do you need Pepperoni over your Pizza? [Yes/No]\n"))
    if pep == 'Y' or pep == 'y':
        bill1 = bill1 + 3
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    else:
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    che = str(input("DO you need extra cheese over your Pizza? [Yes/No]\n"))
    if che == 'y' or che == 'Y':
        bill1 = bill1 + 1
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    else:
        print(f"The total bill for your {size} size Pizza is ${bill1}")
    print("Thank You for Visiting Pizza House!")
print("Visit Again!!")
