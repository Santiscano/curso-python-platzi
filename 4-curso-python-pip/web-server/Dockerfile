# Version de Python donde se va a ejecutar la aplicación
FROM python:3.10

# Directorio de trabajo
WORKDIR /app
# Copiar el archivo requirements.txt al directorio de trabajo dentro del contenedor
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias del archivo requirements.txt sin caché y actualizar pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar el contenido de la carpeta actual al directorio de trabajo dentro del contenedor
COPY . /app

# Comando que se ejecutará al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]