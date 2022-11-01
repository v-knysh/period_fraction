from dataclasses import dataclass
import datetime
import math


@dataclass
class CommonFraction:
    base:float
    numenator: int
    denumenator: int
    approx_error:float

    @classmethod
    def from_float(cls, 
                   base:float, 
                   max_denumenator:int=60,
                   min_approx_error=0, 
                   max_approx_error=1/365) -> "CommonFraction":
        res = None
        for b in range(max_denumenator, 0, -1):
            a = math.floor(base * b + 0.5)
            approx_error = a/b - base
            approx_matches = (approx_error >= min_approx_error 
                and approx_error < max_approx_error*0.999)
            # print(a, b, approx_error, approx_error < max_approx_error, max_approx_error)
            if res is None or approx_matches:
                res = (a, b, approx_error)
        return cls(base, res[0], res[1], res[2])

    def __str__(self):
        return f"{self.numenator} / {self.denumenator}"

    def value(self):
        return self.numenator / self.denumenatord


class DailyReport:
    def __init__(self, start: datetime) -> None:
        self._start = start

    def __str__(self):
        days = (datetime.datetime.now() - self._start).days
        common_fraction = CommonFraction.from_float(days/365, 365)
        return f"Today is day #{days}, its {days/365*100:.2f}% or {common_fraction} of the year"


if __name__ == "__main__":
    start = datetime.datetime(2022,3,13)

    for i in range(1, 2):
        datestring = ((start + datetime.timedelta(days=i)).strftime("%y-%m-%d"))

        f = CommonFraction.from_float(i/365, 365)
        if f.denumenator > 20:
            print(datestring)
        else:
            print(f"{datestring}, {f}")
    
    print()
    print()
    print()
    print()
    print(DailyReport(start)) 
    