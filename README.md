# fastapi-example
Una api sencilla con FastAPI

## Construcción de la Imagen Docker
Navega a la carpeta donde están ubicados el Dockerfile y requirements.txt, y ejecuta el siguiente comando para construir la imagen Docker:

'''
docker build -t fastapi-smartthing-app .
'''

Esto creará una imagen Docker con el nombre fastapi-smartthing-app.

## Ejecutar el Contenedor
Una vez que la imagen esté construida, puedes ejecutar un contenedor a partir de ella con el siguiente comando:

'''
docker run -d -p 8000:8000 fastapi-smartthing-app
'''

Esto ejecutará tu aplicación FastAPI en un contenedor Docker y expondrá el puerto 8000.

## Verificar que Todo Está Funcionando
Después de ejecutar el contenedor, puedes verificar que la aplicación está corriendo accediendo a:

Interfaz de Documentación de FastAPI: http://localhost:8000/docs
Interfaz de Redireccionamiento de OpenAPI: http://localhost:8000/redoc

