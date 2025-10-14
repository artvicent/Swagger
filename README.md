Arturo Valero 13909409
Programación V Base de datos en ambiente web
descargar el .rar ya que GitHub no me dejo subir carpetas que tengas mas de 100 archivos


Paso a paso para iniciar la API Django REST Framework
1️⃣ Abrir PowerShell

Abre PowerShell 

2️⃣ Navegar a la carpeta de tu proyecto


cd "D:\Mis Documentos\UBA\9no trimestre\PROGRAMACION V\Sumativa III\weather_api"

3️⃣ Activar el entorno virtual

Si tu entorno virtual se llama venv y está en Sumativa III:

..\venv\Scripts\Activate.ps1


Verás que la terminal cambia y aparece (venv) al inicio de la línea.
Esto indica que estás usando el Python y librerías instaladas en tu entorno virtual.

4️⃣ Verificar que Django está instalado

Para asegurarte de que tu entorno tiene Django y DRF:

pip list

Django          5.2.7
djangorestframework 3.16.1


Si falta algo, instálalo:

pip install django djangorestframework

5️⃣ Ejecutar el servidor

Con el entorno virtual activo y dentro de la carpeta que contiene manage.py, ejecuta:

python manage.py runserver


Salida esperada:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 09, 2025 - 23:50:00
Django version 5.2.7, using settings 'weather_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

6️⃣ Probar la API

Abrir tu navegador o Postman y probar:

Listar temperaturas (GET):

http://127.0.0.1:8000/api/temperatures/


Obtener token:

http://127.0.0.1:8000/api-token-auth/


Crear, actualizar o eliminar registros usando tu token.

7️⃣ Detener el servidor

Para detener el servidor en PowerShell, presiona:

CTRL + C

8️⃣ Cerrar el entorno virtual

Cuando termines, para salir del entorno virtual:

deactivate


Esto vuelve a usar tu Python del sistema.
usuario user
Contraseña Boston1.

## Documentación automática (Swagger)

La API está documentada con **drf-yasg**. Puedes ver la documentación en:

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- Redoc: `http://127.0.0.1:8000/redoc/`

### Capturas
![Swagger - Lista de endpoints](docs/swagger_list.png)
![Swagger - Crear temperatura](docs/post-api-temperatures-id.png)
![Redoc](docs/redoc.png)
