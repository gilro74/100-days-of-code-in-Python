print("Welcome to our Theme Park!")

height =int(input("Please enter your height: "))

if height <= 120:
    print("Unfortunately you are too short to use the rides!")
else:
    age =int(input("What is your age? "))
    if age >= 18:
        print("You are suppose to pay $12.00 ")
    else:
        if 12<=age<18:
            print("You are suppose to pay $7.00.")
        else:
            print("You are suppose to pay $5.00")

