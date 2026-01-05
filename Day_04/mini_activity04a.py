import random
guess = int(input("Please choose a number between 1 and 5 :\n").strip())

random_gen = random.randint(1,5)

if random_gen == guess:
    print("Congratulation, you have won. You can get a gulp of coke! ")
else:
    print("Please try again!")


print(f"Your guess was {guess} and the answer was suppose to be {random_gen}")