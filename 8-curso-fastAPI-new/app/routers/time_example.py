from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import APIRouter

time_router = APIRouter()

countr_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
    "CL": "America/Santiago",
}

def get_time_in_timezone(iso_code: str, format_code: str = "24"):
    iso = iso_code.upper() # convierte a mayusculas
    countr_timezones
    timezone_str = countr_timezones.get(iso) # obtiene la zona horaria segun el diccionario
    if timezone_str is None: # valida si la zona horaria es nula
        return {"error": f"Invalid ISO code: {iso_code}"}
    tz = ZoneInfo(timezone_str) # obtiene la zona horaria con la libreria zoneinfo
    if format_code == "24":
        return {"time": datetime.now(tz=tz).strftime("%H:%M:%S")} # retorna la hora en formato 24 horas con strftime y su resultado se veria asi: 14:30:00
    elif format_code == "12":
        return {"time": datetime.now(tz=tz).strftime("%I:%M:%S %p")} # retorna la hora en formato 12 horas con strftime y su resultado se veria asi: 02:30:00 PM
    return {"error": f"Formatcode {format_code} not supported"}

@time_router.get("/time", tags=["time"])
async def time_without_params():
    current_time = datetime.now().strftime("%H:%M:%S")
    return {"time": current_time}

# uso de parametros
@time_router.get("/time/{iso_code}", tags=["time"])
async def time_without_format(iso_code: str):
    return {"time": get_time_in_timezone(iso_code)}


@time_router.get("/time/{iso_code}/{format_code}", tags=["time"])
async def time_with_format(iso_code: str, format_code: str):
    return get_time_in_timezone(iso_code, format_code)