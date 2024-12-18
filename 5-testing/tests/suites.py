import unittest

from tests.test_bank_account import BankAccountTests


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
    
    
# Correr solo esta suite de pruebas
# primero se deben crear los archivos __init__.py en las carpetas src y tests
# luego se debe ejecutar el siguiente comando en la terminal
# PYTHONPATH=. python tests/suites.py