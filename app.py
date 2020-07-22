name = input("Please enter your name: ")

if len(name) > 10:
    print("Name cannot exceed 10 characters")
elif len(name) < 3:
    print("Name must be at least 3 characters.")

else:
    print("Hello ", name)