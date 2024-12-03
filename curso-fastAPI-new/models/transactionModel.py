from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

# from .customerModel import CustomerModel

class TransactionBaseModel(SQLModel):
    ammount             : float = Field(default=None)
    description         : str = Field(default=None)

class TransactionModel(TransactionBaseModel, table=True):
    
    id                  : int = Field(default=None, primary_key=True)
    # customer_id         : int = Field(default=None, foreign_key="customer.id") #* se indica tabla.key
    # customer            : "CustomerModel" = Relationship(back_populates="transactions") #* Relationship nos permite hacer la relacion entre tablas, en este caso estamos diciendo que la tabla de transations tiene una relacion con la tabla de customers
    #* back_populates="transactions" indicamos la columna de la otra tabla con la que se relaciona


class TransactionCreateModel(TransactionBaseModel):
    customer_id        : int = Field(default=None, foreign_key="customer.id") #* se indica tabla.key

