print("Welcome to the tip Calculator!")
#Note- Keeping same datatype when working with numbers is very important!,like now
#Working with float only helps in avoiding errors
total_bill = float(input("What is your total bill? $"))
percentage_tip = float(input("How much tip would you like to give? 10, 12 or 15? "))

if percentage_tip == 10:
    new_total_bill = float(total_bill * 1.1) #1.1 means 110%, same with other percentanges
    number_of_people =float(input("How many people would you like to split the bill? "))
    cost_per_person =new_total_bill / number_of_people
    print(cost_per_person)
    
elif percentage_tip == 12:
    new_total_bill = float(total_bill * 1.12)
    number_of_people =float(input("How many people would you like to split the bill? "))
    cost_per_person =new_total_bill / number_of_people
    print(cost_per_person)

elif percentage_tip == 15:
    new_total_bill = float(total_bill * 1.15)
    number_of_people =float(input("How many people would you like to split the bill? "))
    cost_per_person =new_total_bill / number_of_people
    print(cost_per_person)
                                                                                                  