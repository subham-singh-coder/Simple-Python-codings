#Print the name of the individual from a list who should be paying the Bill of food today
import random
name_str=str(input("Enter the name of individuals using comma and Space:\n"))
name=name_str.split(",")
person=random.choice(name)
print(f"{person} would be paying the bill today")
