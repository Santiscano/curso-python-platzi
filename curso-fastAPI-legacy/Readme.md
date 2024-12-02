# Curso fastapi python

## iniciar con el proyecto desde cero o arrancarlo
1. Generar entorno virtual "es necesario tener instalado de manera global venv".
```shell
$ python -m venv <name_enviroment>
```

2. Activar entorno.
```shell
# windows
$ <nameEnv>/Script/activate
# linux
$ source <nameEnv>/bin/activate
```

3. instalar modulos.
```shell
# proyecto desde cero
$ pip install fastapi
# arrancar este proyecto
$ pip install -r requirements.txt
# instalar un nuevo modulo
$ pip install sqlalchemy
# actualizar requirements.txt
$ pip freeze > requirements.txt # es necesario estar dentro del venv
# desactivar el entorno virtual
$ deactivate
```

4. Arrancar app.
```shell
$ fastapi dev main.py --reload
```

5. Despliegue en un Droplet o VPS
```shell
# actualizar e instalar herramientas necesarias
$ apt update
$ apt -y upgrade
$ apt install git
$ apt install nginx
$ apt install nodejs
$ apt install npm
$ apt install pm2@latest -g
$ apt install python3-venv
# crear entorno virtual
$ python3 -m venv venv
# activar entorno virtual
$ source venv/bin/activate
# instalar dependencias
$ pip install -r requirements.txt # -r es leer el archivo requirements.txt
```

6. Correr en servidor con Nginx
```shell
$ pm2 start "fastapi dev main.py --reload" --name my-api-fastapi
# configurar nginx
$ nano /etc/nginx/sites-available/my-api-fastapi
```

```.config
server {
    listen 80;
    server_name 142.42.124.79;

    location / {
        proxy_pass http://127.0.0.1:5000;
    }
}
```
```shell
# despues de crear el archivo hay que ejecutar el siguiente comando
$ sudo ln -s /etc/nginx/sites-available/my-api-fastapi /etc/nginx/sites-enabled/
# reiniciar nginx
$ sudo systemctl restart ngin
```