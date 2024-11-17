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
            value (float): The amount of the loan..
        Raises:
            ValueError: When the value provided is 
            not a valid in loan amount.
        """
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        else:
            self.__loan_amount = value

    ## ACCESSOR
    @property
    def string_rate_value(self) -> str:
        """
        Accessor for rate attribute.
        """
        return self.__string_rate_value

    ## MUTATORS
    @string_rate_value.setter
    def string_rate_value(self, string_value:str):
        """    
        Sets the string_value for rate.
        Args:
            string_value (str):The annual interest rate string equivalent to enum value.
        Raises:
            ValueError: When the rate provided is 
            not a valid in enum.
        """
        try:
            self.__string_rate_value = MortgageRate[string_value]
        except:
            raise ValueError("Rate provided is invalid.")
        
    # ACCESSORS
    @property
    def string_frequency_value(self) -> str:
        """
        Accessor for frequency attribute.
        """
        return self.__string_frequency_value
    
    # Mutators
    @string_frequency_value.setter
    def string_frequency_value(self, frequency:str):
        """    
        Sets the frequency.
        Args:
            frequency (str): frequency provided by user for their loan.
        Raises:
            ValueError: When the frequency provided is 
            not a valid in enum.
        """
        try:
            self.__string_frequency_value = PaymentFrequency[frequency]
        except:
           raise ValueError("Frequency provided is invalid.") 
    
    # ACCESSORS
    @property
    def amortization(self) -> int:
        """
        Accessor for amortization attribute.
        """    
        return self.__amortization
    
    # MUTATORS
    @amortization.setter
    def amortization(self,value:int):
        """    
        Sets the value
        Args:
            value (int): value provided by user for their loan.
        Raises:
            ValueError: When the value provided is 
            not a valid in enum.
        """
        if value in VALID_AMORTIZATION:
            self.__amortization = value
        else:
            raise ValueError("Amortization provided is invalid.") 
        
    def calculate_payment(self) -> float:
        """
        This function is calculated the payment  with respect to Loan Amount, 
        Interest Rate, Frequency and Amortization.
        Retuns:
            float: the actual payment in decimals.
        """

        payment = Mortgage(682912.43, "FIXED_1", "MONTHLY", 10)

        rate = self.__string_rate_value.value

        frequency = self.__string_frequency_value.value
        i = rate / frequency
        n = self.amortization * frequency
    
        formula =  (i * (1+i)**n)/(((1+i)**n)-1)

        calculated_payment = self.loan_amount * formula
        calculated_payment  = f"{calculated_payment:.2f}"
        calculated_payment = float(calculated_payment)

        return calculated_payment
    
    def __str__(self):
        """
        This function prints as a String representation.
        Returns:
              str: Returns a string representation of the class.
              format and example: Mortgage Amount: $682,912.43
                      Rate: 5.89%
                      Amortization: 30
                      Frequency: Monthly -- Calculated Payment: $4,046.23
        """
        return (f"Mortgage Amount: ${self.__loan_amount:,.2f}"
        + f"\nRate: {self.__string_rate_value.value * 100}%"
        + f"\nAmortization: {self.__amortization}"
        + f"\nFrequency: {str(self.__string_frequency_value).split(".")[-1]} -- Calculated Payment: ${self.calculate_payment():,.2f}")
    

    def __repr__(self):
        """
            
        Provides a representation of an Mortgage object.
        Returns:
            str: A representation of a loan amount.
                format: Mortgage({loan-amount}, {interest-rate}, {frequency}, {amortization})
                example: Mortgage(682912.43, 0.0599, 12, 30)
        """
        return   (f"Mortgage({self.__loan_amount:.2f}, "
                  + f"{self.__string_rate_value.value}, "
                  + f"{self.__string_frequency_value.value}, "
                  + f"{self.__amortization})")