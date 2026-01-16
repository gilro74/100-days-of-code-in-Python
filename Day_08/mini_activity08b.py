def life_in_weeks(age):
    result = (90-age)*52 
    
    print(f"You have {result} weeks left.")
age = int(input("what is your age? "))
life_in_weeks(age)