from pydantic import BaseModel

from .customerModel import CustomerModel
from .transactionModel import TransactionModel

class InvoiceModel(BaseModel):
    id: int
    customer: CustomerModel
    transactions: list[TransactionModel]
    total: int
    
    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)