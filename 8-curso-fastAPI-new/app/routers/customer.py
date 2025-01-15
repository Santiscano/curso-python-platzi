
from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from config.db_sqlite import SessionDep
from models.customerModel import  CustomerCreateModel, CustomerModel

customer_router = APIRouter(tags=["customers"]) #* en vez de ponerselo a cada ruta, se lo ponemos al router y todos los endpoints que esten en ese router tendran ese tag


@customer_router.get(
    "/customers",
    response_model=dict[str, list[CustomerModel]], 
    status_code=status.HTTP_200_OK
)
async def get_customers(session: SessionDep):
    db_customers = session.exec(select(CustomerModel)).all()
    return {"customers": db_customers}


@customer_router.get("/customer/{customer_id}", response_model=CustomerModel)
async def get_customer(customer_id: int, session: SessionDep):
    db_customer = session.get(CustomerModel, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return {"customer": db_customer}


@customer_router.post("/customer", response_model=CustomerModel, status_code=status.HTTP_201_CREATED)
async def create_customer(customer_data: CustomerCreateModel, session: SessionDep):
    customer = CustomerModel.model_validate(customer_data.model_dump()) #* esto es para validar que los datos que se envian en el body de la peticion sean correctos
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@customer_router.put("/customer/{customer_id}", response_model=CustomerModel, status_code=status.HTTP_201_CREATED)
async def update_customer(customer_id: int, customer_data: CustomerCreateModel, session: SessionDep):
    db_customer = session.get(CustomerModel, customer_id)
    if db_customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer not found"
        )
    try:
        CustomerModel.model_validate(customer_data.model_dump()) #* model_dump() es para obtener los datos del modelo en un diccionario, model_validate() es para validar los datos
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    else:
        db_customer.sqlmodel_update(customer_data.model_dump(exclude_unset=True)) #* sqlmodel_update() es para actualizar los datos del modelo, con exclude_unset=True estamos diciendo que no se actualicen los campos que no se envian en el body de la peticion
        # for key, value in customer_data.dict().items():
        #     setattr(db_customer, key, value)
        session.add(db_customer)
        session.commit()
        session.refresh(db_customer)
        return {"customer": db_customer}


@customer_router.delete("/customer/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    db_customer = session.get(CustomerModel, customer_id)
    if db_customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    session.delete(db_customer)
    session.commit()
    return {"message": "Customer deleted successfully"}