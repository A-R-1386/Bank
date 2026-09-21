from Bank import Bank

bank = Bank('Saderat')

assert bank.transaction('0000', '3321', 48) == True
assert bank.transaction('3321', '1123', 40) == True

money_3321 = bank.check('3321')
assert money_3321 == 8

assert bank.transaction('3321', '1123', 12) == False

money_1123 = bank.check('1123')
assert money_1123 == 40

assert bank.check('0000') == -1

assert len(bank.history('3321')) == 3
#assert bank.info() == ("Saderat",  2, 3) # bank_name, number_of_accounts, number_of_transactions
