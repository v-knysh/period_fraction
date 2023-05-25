import unittest

from common_fractions import CommonFraction


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

    def test_364_days_is_not_year(self):
        f = CommonFraction.from_float(364/365, max_denumenator=65)
        print(f)
        self.assertNotEqual(f.denumenator, 1)
        # self.assert_equals(
        #     (f.numenator, 1), 
        #     (f.denumenator, 1), 
        #     )
        # 
    def test_364_days_is_not_year(self):
        f = CommonFraction.from_float((365 / 5 * 3 - 1)/365, max_denumenator=365)
        print(f)
        self.assertNotEqual(f.denumenator, 5)