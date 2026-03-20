# Write to file (w = overwrite or create)
with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is a test file\n")

# Append (a = add to end)
with open("sample.txt", "a") as f:
    f.write("New line added\n")

print("File written and appended successfully!")