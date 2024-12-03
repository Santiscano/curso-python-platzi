from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from config.db_sqlite import SessionDep
from models.customerModel import CustomerModel
from models.transactionModel import TransactionModel, TransactionCreateModel

router = APIRouter()


@router.post(
    "/transactions", status_code=status.HTTP_201_CREATED, tags=["transactions"]
)
async def create_transation(transaction_data: TransactionCreateModel, session: SessionDep):
    transaction_data_dict = transaction_data.model_dump()
    customer = session.get(CustomerModel, transaction_data_dict.get("customer_id"))
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist"
        )

    transaction_db = TransactionModel.model_validate(transaction_data_dict)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)

    return transaction_db


@router.get("/transactions", tags=["transactions"])
async def list_transaction(session: SessionDep):
    query = select(TransactionModel)
    transactions = session.exec(query).all()
    return transactions