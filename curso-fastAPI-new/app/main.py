from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import jwt

from app.routers.time_example import time_router
from app.routers.customer import customer_router
from app.routers.transactions import router as transaction_router
from config.db_sqlite import create_all_tables

app = FastAPI(lifespan=create_all_tables)

SECRET_KEY = "your_secret_key"  # Clave para firmar y verificar el token
ALGORITHM = "HS256"  # Algoritmo de firma (coincide con el utilizado para generar el token)
class TokenValidationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Obtén el token del encabezado de autorización
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                content={"detail": "Token de autorización no encontrado o inválido"},
                status_code=401
            )
        
        # Extrae el token después de "Bearer "
        token = auth_header.split(" ")[1]
        
        try:
            # Decodifica y valida el token
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            # Puedes agregar validaciones personalizadas aquí si es necesario
        except jwt.ExpiredSignatureError:
            return JSONResponse(
                content={"detail": "El token ha expirado"},
                status_code=401
            )
        except jwt.InvalidTokenError:
            return JSONResponse(
                content={"detail": "El token es inválido"},
                status_code=401
            )
        
        # Si el token es válido, continúa al siguiente middleware o ruta
        response = await call_next(request)
        return response



@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(time_router)
app.include_router(customer_router)
app.include_router(transaction_router)
