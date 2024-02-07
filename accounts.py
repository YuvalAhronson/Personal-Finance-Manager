#!/usr/bin/env python
"""
This the accounts module.
"""
class Account:
    def __init__(self, amount, account_type, expiray_date):
        self.amount = amount
        self. account_type = account_type
        self.expiray_date = expiray_date
    

class CreditCardAccount(Account):
    def __init__(self, amount, account_type, expiray_date, credit_card_num, id_on_card, cvv, ):
        super().__init__(amount, account_type, expiray_date)

class CheckingAccount(Account):
    pass

class SavingAccount(Account):
    pass

class InvesmentAccount(Account):
    pass


