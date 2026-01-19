def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

name = input("What is your name? ").strip()
location = input("Location? ").strip()

greet_with(name,location)