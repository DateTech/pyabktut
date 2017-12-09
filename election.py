print("   INDEPENDENT NATIONAL ELECTORIAL COMMISION   ")
print("------------------------------------------------")
print("\n")

name = input("What is your name: ")
age = input("How old are you: ")
age = int(age)

print("\n")

if(age >= 18) and (age <= 60):
    print("Hey ", name,", You are eligible for the election")
else:
    print(name, "is not eligible for the election")

