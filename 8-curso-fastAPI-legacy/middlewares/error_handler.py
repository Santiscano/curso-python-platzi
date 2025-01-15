from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app:FastAPI) -> None:
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            response = await call_next(request)
        except Exception as e:
            response = self.exception_handler(request, e)
        return response

    def exception_handler(self, request, exc):
        return JSONResponse(
            content={"error": str(exc)},
            status_code=500
        )