def computepay(hours, rate):
    if hours>40.0:
        reg_pay = rate*40
        ovrtime_pay = (hours-40.0)*(rate*1.5)
        Total_pay = reg_pay + ovrtime_pay
    else:
        Total_pay = hours * rate

    return Total_pay


hrs = input("Enter Hours: ")
rte = input("Enter rate per hour: ")

hrs = float(hrs)
rte = float(rte)

pay = computepay(hrs,rte)
print("Pay:",pay)
