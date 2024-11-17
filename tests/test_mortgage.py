"""
Description: A class used to test the Mortgage class.
Author: Gaganpreet Kaur
Date: 11-11-2024
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
# IMPORTS
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    ## Tests needed:
    ## _init test_

    def test_init_invalid_amount_input (self):
         # Arrange 
         expected = "Loan Amount must be positive."
         # Act and Asserts
         with self.assertRaises(ValueError) as context:
             Mortgage(-2, "FIXED_3", "MONTHLY", 25)
         self.assertEqual(expected, str(context.exception))

    def test_init_invalid_rate_input(self):
        # Arrange
        expected = "Rate provided is invalid."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(10000, "INVALID_RATE", "MONTHLY", 25)
        self.assertEqual(expected, str(context.exception))

    def test_init_invalid_frequency_input(self):
        # Arrange
        expected = "Frequency provided is invalid."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(10000, "FIXED_5", "INVALID_FREQUENCY", 25)
        self.assertEqual(expected, str(context.exception)) 

    def test_init_invalid_amortization_input_value(self):
        # Arrange
        expected = "Amortization provided is invalid."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(10000, "FIXED_3", "MONTHLY", 100)
        self.assertEqual(expected, str(context.exception))

    def test_init_valid_attributes(self):
        # Arrange
        valid_amount = 10000
        valid_rate = "FIXED_3"
        valid_frequency = "MONTHLY"
        valid_amortization = 10
        mortgage = Mortgage(valid_amount, valid_rate, valid_frequency, valid_amortization)
        actual_rate = str(mortgage.string_rate_value).split(".")[-1]
        print(actual_rate)
        actual_frequency = str(mortgage.string_frequency_value).split(".")[-1]
        print(actual_frequency)
        print(f"Expected Rate: {valid_rate}, Actual Rate: {actual_rate}")
        print(f"Expected Frequency: {valid_frequency}, Actual Frequency: {actual_frequency}")
        # Act and Assert
        self.assertEqual(mortgage.loan_amount,10000)
        self.assertEqual(actual_rate, "FIXED_3")
        self.assertEqual(actual_frequency, "MONTHLY")
        self.assertEqual(mortgage.amortization, 10)