age = int(input("Enter age of a user: "))

def eligible(age):
    if age >= 18:
         print("User is eligible for voting: ", age)
    else:
         print("User is not eligible for voting: ", age)