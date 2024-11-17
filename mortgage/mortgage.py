"""
Description: A class meant to manage Mortgage options.
Author: Gaganpreet Kaur
Date: 11-11-2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
# IMPORTS
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

# CLASS
class Mortgage:
    def __init__(self,loan_amount: float,string_rate_value: str, string_frequency_value: str, amortization: int):
        """
        Initialize a new Mortgage object with an loan_amount,string_rate_value,string_frequency_value,amortization.
        Args:
            loan_amount (float): The amount of the mortgage loan.
            string_rate_value (str): The annual interest rate string equivalent to enum value.
            string_frequency_value (str):  The number of payments per year string equivalent to enum value.
            amortization (int): The number of years to repay the mortgage loan. 
        
        Returns:
            None

        Raises:
            ValueError: When loan amount is invalid.
            ValueError: When rate is invalid.
            ValueError: When frequency is invalid.
            ValueError: When amortization is invalid.


        """
        if loan_amount <= 0:
             raise ValueError("Loan Amount must be positive.")
        else:
            self.__loan_amount = loan_amount

        try:
            self.__string_rate_value = MortgageRate[string_rate_value]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        try:
            self.__string_frequency_value = PaymentFrequency[string_frequency_value.upper()]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
          
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        else:
            self.__amortization = amortization


    ## ACCESSOR
    @property
    def loan_amount(self) -> float:
        """
        Accessor for loan_amount attribute.
        """
        return self.__loan_amount
    
    ## MUTATOR
    @loan_amount.setter
    def loan_amount(self, value: float):
        """    
        Sets the value for loan amount.
        Args:
            value (sloat): The amount of the loan..
        Raises:
            ValueError: When the value provided is 
            not a valid in loan amount.
        """
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        else:
            self.__loan_amount = value