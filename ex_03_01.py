hrs = input("Enter Hours: ")
rate = input("Enter rate per hour: ")

hrs = float(hrs)
rate = float(rate)
if hrs>40.0:
    reg_pay = rate*40
    ovrtime_pay = (hrs-40.0)*(rate*1.5)
    Total_pay = reg_pay + ovrtime_pay
else:
    Total_pay = hrs * rate

print("Pay:",Total_pay)
