def greet(name):
   return "Hello " + name

def call_func(func):
    other_name = "John"
    return func(other_name)

print call_func(greet)

def greet(name):
    return "hello "+name

greet_someone = greet
print greet_someone("John")


def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet = compose_greet_func("John")
print greet()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = 7
print factorial(n)