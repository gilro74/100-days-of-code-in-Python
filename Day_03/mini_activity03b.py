print("Welcome to our Theme Park!")

height =int(input("Please enter your height: "))
bill = 0
if height <= 120:
    print("Unfortunately you are too short to use the rides!")
else:
    age =int(input("What is your age? "))
    if age >= 18:
        bill = 12
        print("You are suppose to pay $12.00 ")
    else:
        if 12<=age<18:
            bill = 7
            print("You are suppose to pay $7.00.")
        else:
            bill = 5
            print("You are suppose to pay $5.00")
    wants_photo =input("Do you want a ticket? Yes or No :")
    if wants_photo == "Yes":
        new_bill = bill + 3
        print(new_bill)
    else:
        print(bill)
    




