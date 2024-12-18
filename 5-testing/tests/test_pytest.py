# documentacion https://docs.pytest.org/en/latest

import pytest
from src.bank_account import BankAccount

# parametrize recibe 2 argumentos, el primero es el nombre de la variable que se va a parametrizar y el segundo es una lista de tuplas con los valores que se van a probar
@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_ammounts(ammount, expected): # los nombres del primer parametro son los parametros que se ponen aqui
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected



