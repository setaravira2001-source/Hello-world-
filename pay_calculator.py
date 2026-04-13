hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hour=float(input("Enter the rate per hour"))
if h<=40:
    pay=h*rate_per_hour
else:
    overtime=h-40
    pay=(40*rate_per_hour)+(overtime*rate_per_hour*1.5)
print(pay)