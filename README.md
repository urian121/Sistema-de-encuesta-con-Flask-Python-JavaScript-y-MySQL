
# Guía para Configurar y Ejecutar el Proyecto

## Paso 1: Crear el entorno virtual
Ejecuta uno de los siguientes comandos para crear tu entorno virtual:
```bash
virtualenv -p python3 env
```
O alternativamente:
```bash
python3 -m venv env
```

## Paso 2: Activar el entorno virtual
Activa el entorno virtual con el siguiente comando:

- En Windows:
  ```bash
  . env/Scripts/activate
  ```
- En Mac/Linux:
  ```bash
  source env/bin/activate
  ```

## Paso 3: Instalar Flask
Una vez que el entorno virtual esté activado, instala Flask:
```bash
pip install flask
```

Es recomendable actualizar `pip` a la última versión:
```bash
python -m pip install --upgrade pip
```

## Paso 4: Instalar el conector MySQL para Python
Instala el driver necesario para conectar Python con MySQL:
```bash
pip install mysql-connector-python
```

## Paso 5: Listar los paquetes instalados
Para ver los paquetes instalados en tu entorno virtual, puedes usar:
```bash
pip list
```
O generar un archivo `requirements.txt` con todas las dependencias del proyecto:
```bash
pip freeze > requirements.txt
```

## Paso 6: Instalar dependencias desde `requirements.txt`
Para configurar rápidamente el entorno con las dependencias necesarias para el proyecto, usa el siguiente comando:
```bash
pip install -r requirements.txt
```

## Nota Importante:
El archivo `requirements.txt` contiene todas las dependencias del proyecto, por lo que ejecutar el comando anterior instalará todo lo necesario para correr el proyecto.

---

¡Ahora estás listo para iniciar el desarrollo!
