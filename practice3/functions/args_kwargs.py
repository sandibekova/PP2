def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

def mys_function(**kid):
  print("His last name is " + kid["lname"])

mys_function(fname = "Tobias", lname = "Refsnes")