def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Test with for loop
for result in squares(2, 6):
    print(result)