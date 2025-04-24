# def greet(name, greeting):
#     print(f"{greeting}, {name}!")
#
# greet("Alex", "Hello")
# greet("Goodbye", "Anna")

# def greet(name, greeting):
#     print(f"{greeting}, {name}!")
#
# greet(name="Alex", greeting="Hello")
# greet(greeting="Goodbye", name="Anna")

# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")
#
# greet("Alex")
# greet("Anna", "Goodbye")
# greet(name="Olga")
# greet(greeting="Hi", name="Roman")

def new_function(a):
    res = a.sorted()
    print(res[len(res)-1])
a = set(map(int, input().split()))
new_function(a)