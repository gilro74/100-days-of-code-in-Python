#Function that allow input

def greet(name):
    print(f'Hello {name}')


name = input("What is your name? ").strip()
greet(name)