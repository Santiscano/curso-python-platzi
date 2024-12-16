# Ecosistema python
[pip](pypi.org)

# Game Project
Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
$ cd game
$ python3 main.py
```


# Charts
```sh
$ pip3 install matplotlib
```

# App Project

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

para correrlo por medio de docker se puede ejecutar los siguientes comandos
```sh
$ docker-compose build # construir el contenedor
$ docker-compose up -d # levantar el contenedor de manera ditach
$ docker-compose ps # ver los contenedores corriendo
$ docker-compose exec name-service bash # ingresar al ambiente
```


### Pasar las dependencias al archivo requirements.txt
```sh
$ pip freeze > requirements.txt
```