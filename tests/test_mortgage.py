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

        actual_frequency = str(mortgage.string_frequency_value).split(".")[-1]
        
        # Act and Assert
        self.assertEqual(mortgage.loan_amount,10000)
        self.assertEqual(actual_rate, "FIXED_3")
        self.assertEqual(actual_frequency, "MONTHLY")
        self.assertEqual(mortgage.amortization, 10)


    def test_loan_amount_negative_value(self):
        # Arrange
        loan = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        expected ="Loan Amount must be positive."

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            loan.loan_amount = -7
        self.assertEqual(expected, str(context.exception))

    def test_loan_amount_zero_value(self):
        # Arrange
        loan = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        expected ="Loan Amount must be positive."

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            loan.loan_amount = 0
        self.assertEqual(expected, str(context.exception))


    def test_loan_amount_positive_value(self):
        # Arrange
        valid_amount = 10000
        valid_rate = "FIXED_3"
        valid_frequency = "MONTHLY"
        valid_amortization = 10
        loan = Mortgage(valid_amount, valid_rate, valid_frequency, valid_amortization)
        loan.loan_amount= 2
        expected = 2

      # Act and Assert
        self.assertEqual(expected,loan.loan_amount)

    def test_string_rate_value_correct_value(self):
        # Arrange
        rate = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        expected = "FIXED_3"
        actual_rate = str(rate.string_rate_value).split(".")[-1]

        # Act and Assert
        self.assertEqual(expected, actual_rate)


    def test_string_rate_value_incorrect_value(self):
        # Arrange
        rate = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        expected = "Rate provided is invalid."

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            rate.string_rate_value = "INVALID_RATE"
        self.assertEqual(expected, str(context.exception))
    
    def test_string_frequency_value_correct(self):
        # arrange
        frequency = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        # act
        frequency.string_frequency_value = "MONTHLY"
        expected = "MONTHLY"
        actual_frequency = str(frequency.string_frequency_value).split(".")[-1]
        # assert
        self.assertEqual(expected, actual_frequency)



    def test_string_frequency_value_incorrect(self):
        # Arrange
        frequency = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        expected = "Frequency provided is invalid."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            frequency.string_frequency_value = "INVALID_FREQUENCY"
        self.assertEqual(expected, str(context.exception))

    def test_amortization_correct(self):
        # Arrange
        amortization = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        # Act
        expected = 10
        # Assert
        self.assertEqual(expected,amortization.amortization)

    def test_amortization_incorrect(self):
        # Arrange
        amortization = Mortgage(10000, "FIXED_3", "MONTHLY", 10)
        expected = "Amortization provided is invalid."

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            amortization.amortization = 100
        self.assertEqual(expected, str(context.exception))
          
    def test_calculate_payment_valid(self):
        # Arrange
        payment = Mortgage(682912.43, "FIXED_1", "MONTHLY", 10)
        # Act
        expected = 7578.30
        # Assert
        actual = payment.calculate_payment()
        self.assertEqual(actual,expected)



    def test_calculate_payment_decimal_places (self):
        # Arrange
        payment = Mortgage(682912.43, "FIXED_1", "MONTHLY", 10)
        # Act
        expected = 7578.30
        actual = payment.calculate_payment()
        # Assert
        self.assertAlmostEqual(actual,expected)
