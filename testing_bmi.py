import unittest
from main import calculate_bmi
from main import categorize_bmi



class TestCalculateBMI(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(6,1,126), 16.6)

    #Testing Negative Values

    def test_negative_height(self):
        self.assertRaises(ValueError, calculate_bmi, -2, 2, 2)

    def test_negative_inch(self):
        self.assertRaises(ValueError, calculate_bmi, 2, -2, 2)

    def test_negative_weight(self):
        self.assertRaises(ValueError, calculate_bmi, 2, 2, -2)

    #Testing String Values

    def test_str_height(self):
        self.assertRaises(ValueError, calculate_bmi, 'two', 2, 2)

    def test_str_inch(self):
        self.assertRaises(ValueError, calculate_bmi, 2, 'two', 2)

    def test_str_weight(self):
        self.assertRaises(ValueError, calculate_bmi, 2, 2, 'two')

    #Testing with 0

    def test_zero_height_and_inch(self):
        self.assertRaises(ValueError, calculate_bmi, 0, 0, 2)

    def test_zero_weight(self):
        self.assertRaises(ValueError, calculate_bmi, 2, 2, 0)

    #Testing Weight with Decimal Numbers

    def test_weight_float(self):
        self.assertAlmostEqual(calculate_bmi(5, 9, 160.5), 23.7, places=1)


class TestCategorizeBMI(unittest.TestCase):
    # Testing Weak N x 1
    def test_categorize_bmi(self):
        #0 is ON
        self.assertEqual(categorize_bmi(0), "Underweight")

    def test_underweight_01(self):
        #0.1 is OFF
        self.assertEqual(categorize_bmi(0.1), "Underweight")

    def test_underweight_0(self):
        #Interior
        self.assertEqual(categorize_bmi(10), "Underweight")

    def test_underweight_184(self):
        #18.4 is OFF
        self.assertEqual(categorize_bmi(18.4), "Underweight")

    def test_underweight_185(self):
        #18.5 is ON
        self.assertEqual(categorize_bmi(18.5), "Normal weight")

    def test_weight_184(self):
        #184 is OFF
        self.assertEqual(categorize_bmi(18.4), "Underweight")

    def test_weight_185(self):
        #185 is ON
        self.assertEqual(categorize_bmi(18.5), "Normal weight")

    def test_weight_20(self):
        #Interior
        self.assertEqual(categorize_bmi(20), "Normal weight")

    def test_weight_249(self):
        #24.9 is ON
        self.assertEqual(categorize_bmi(24.9), "Normal weight")

    def test_weight_25(self):
        #25 is OFF
        self.assertEqual(categorize_bmi(25), "Overweight")

    def test_overweight_249(self):
        #24.9 is OFF
        self.assertEqual(categorize_bmi(24.9), "Normal weight")

    def test_overweight_25(self):
        #25 is ON
        self.assertEqual(categorize_bmi(25), "Overweight")

    def test_overweight_28(self):
        #Interior
        self.assertEqual(categorize_bmi(28), "Overweight")

    def test_overweight_299(self):
        #29.9 is ON
        self.assertEqual(categorize_bmi(29.9), "Overweight")

    def test_overweight_30(self):
        #30 is OFF
        self.assertEqual(categorize_bmi(30), "Obese")

    def test_obese_37(self):
        #Interior
        self.assertEqual(categorize_bmi(37), "Obese")

    def test_obese_10000(self):
        #Testing MAX
        self.assertEqual(categorize_bmi(10000), "Obese")


