from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

from .transactionModel import TransactionModel

class CustomerBaseModel(SQLModel):
    name            : str = Field(default=None, max_length=50)
    # description   : str | None #* de esta forma estamos diciendo que recibe un string o un None
    description     : Optional[str] = Field(default=None) #* de esta forma estamos diciendo que recibe un string o un None y ademas nos ayuda a no tener que agregar el campo en el body de la peticion
    email           : str = Field(default=None)
    age             : int = Field(default=None)


class CustomerCreateModel(CustomerBaseModel):
    pass


class CustomerModel(CustomerBaseModel, table=True):
    
    id              : int = Field(default=None, primary_key=True) #* Field es el que nos permite unir el modelo con la tabla de la base de datos
    transations     : list["TransactionModel"] = Relationship(back_populates="customer") #* Relationship nos permite hacer la relacion entre tablas, en este caso estamos diciendo que la tabla de transations tiene una relacion con la tabla de customers
    #* transactions es una lista de transacciones, por lo que es 1 a muchos,
    #* se indica que es list["TransactionModel"] para indicar la relacion con la tabla
    #* back_populates="customer" se pone asi indicando que se vincula a la columna customer de la otra tabla