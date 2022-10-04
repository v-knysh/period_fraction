import datetime

start = datetime.datetime(2022,3,13)


def fraction(value, latest=60):
   res = (0, 0, 0)
   for b in range(latest, 0, -1):
       a = int(value * b + 0.5)
       precision = a/b - value
       pr_lte_day = precision >= 0 and precision < 1/365
       if pr_lte_day:
           res = [a, b, precision]
   return res


print(fraction(0.5))


for i in range(1, 366):
    datestring = ((start + datetime.timedelta(days=i)).strftime("%y-%m-%d"))

    f = fraction(i/365, 365)
    if f[1] > 20:
        print(datestring)
    else:
        print(f"{datestring}, {f[0]} / {f[1]}, {f[2]*100 : .3f}")

