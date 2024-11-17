"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: {Student Name}
Date: {Date}
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""

# IMPORTS
from enum import Enum

VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}# SET

class MortgageRate(Enum):
    """
    An enumeration to store the mortgage rate values.

    Values:
        FIXED_5:    Mortgage Rate
        FIXED_3:    Mortgage Rate
        FIXED_1:    Mortgage Rate
        VARIABLE_5: Mortgage Rate
        VARIABLE_3: Mortgage Rate
        VARIABLE_1: Mortgage Rate
    """
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.0679

class PaymentFrequency(Enum):
    """
    An enumeration to store the payment frequency options.
    Values:
        MONTHLY: Payment frequency option
        BI_WEEKLY: Payment frequency option
        WEEKLY: Payment frequency option
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52