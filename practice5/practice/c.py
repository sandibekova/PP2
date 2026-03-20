import re
emails =["test@gmail.com","user.name@yahoo.com",
    "User@gmail.com",
    "hello@outlook.com",
    "good.mail@gmail.com"]
pattern = r'^[a-z.]+@(gmail\.com|yahoo\.com)$'
for email in emails:
    if re.match(pattern,email):
        print(email)