from dataclasses import dataclass
import datetime
import unittest


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
        res = (1, 1, 1)
        for b in range(max_denumenator, 0, -1):
            a = int(base * b + 0.5)
            approx_error = a/b - base
            approx_matches = (approx_error >= min_approx_error 
                and approx_error < max_approx_error)
            if approx_matches:
                res = (a, b, approx_error)
        return cls(base, res[0], res[1], res[2])

    def __str__(self):
        return f"{self.numenator} / {self.denumenator}, {self.approx_error * 365}"

    def value(self):
        return self.numenator / self.denumenator


class TestUtils(unittest.TestCase):
    def assert_equals(self, *pairs):
        a, b = zip(*pairs)
        self.assertEqual(a, b)

    def test_half_is_half(self):
        f = CommonFraction.from_float(0.5)
        self.assert_equals(
            (f.numenator, 1), 
            (f.denumenator, 2), 
            (f.approx_error, 0)
            )
    
    def test_182_days_is_half(self):
        f = CommonFraction.from_float(182/365)
        self.assert_equals(
            (f.numenator, 1), 
            (f.denumenator, 2), 
            )
    
    def test_121_days_is_third(self):
        f = CommonFraction.from_float(121/365)
        self.assert_equals(
            (f.numenator, 1), 
            (f.denumenator, 3), 
            )

if __name__ == "__main__":
    unittest.main()
