from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD): ")
date= datetime.strptime(date1,"%Y-%m-%d")
today=datetime.now()
age= today.year- date.year
print("Your age:" , age)