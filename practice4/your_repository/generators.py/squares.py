def square_generator(n):
    for i in range(n + 1):
        yield i * i

# Example
for value in square_generator(5):
    print(value)