import datetime

now = datetime.datetime.now()
print(now.strftime("%d %b %Y"))

user_date = input("due date in dd/mm/yyyy: ")

print(user_date)

converted_date = datetime.datetime.strptime(user_date, '%d/%m/%Y')

print(converted_date.strftime("%d %b %Y"))

