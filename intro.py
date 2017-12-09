print("Enter your name ")
name = input()

print("Enter your gender M for Male amd F for Female ")
gender = input()

if(gender == "M") or (gender == "m"):
    print(name,"is a Male")
elif(gender == "F") or (gender == "f"):
    print(name,"is a female")
else:
    print("You are an hermaphodite")