def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

#Positional arguments
greet_with("Felicity", "Seattle")

#Keyword arguments
greet_with(location="London", name="Sam")