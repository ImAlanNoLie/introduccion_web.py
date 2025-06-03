# 1. Hola mundo

## 1.1 Ejemplo básico de web.py

```python
import web

urls = (
    '/hola', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo HTML y Python'

if __name__ == "__main__":
    app.run()
```

## 1.2 Importar libreria

Esta línea permite importar **web.py** para utilizar los métodos para desarrollar aplicaciones web con python

```python
import web
```

## 1.3 Rutas

Cada linea permite manejar la ruta y la clase que controla cada una de las paginas web de la aplicación.

- '/' indica la ruta de acceso a la pagina web
- 'Index' indica el nombre de la clase que maneja el comportamiento de la pagina web


```python
urls = (
    '/hola', 'Index'
)
```

## 1.4 Creacion de la aplicacion web.py

Se crea un objeto del tipo **web.application**, indicando las url, permitiendo que funcione correctamente.

```python
app = web.application(urls, globals())
```

## 1.5 Creación de clase

Cada vez que creamos una pagina web, tambien debemos de crear una clase, de esta manera podremos usar python como herramienta para el desarrollo web.

- Usamos **GET** para **renderizar** la pagina de manera obligatoria.

- En este caso, la clase imprimirá un "Hola mundo HTML y Python" cada vez que usemos el método *GET*

***Nota**: renderizar quiere decir que todo el codigo html, css o javascript, se convierta en la representacion visual que normalmente vemos en nuestro navegador.*

```python
class Index:
    def GET(self):
        return 'Hola mundo HTML y Python'
```

## 1.6 Iniciar la pagina web

Para iniciar nuestra aplicación con python se hace una llamada a app, por lo tanto esta condicion hacer que solo se ejecute cuando usemos python3 app.py.

```python
if __name__ == "__main__":
    app.run()
```

Comando para ejucutar la aplicación:

```python
python3 app.py
```

## 1.7 Ejecutar la aplicación

Una vez hayamos realizado el proceso y ejecutado nuestra aplicación, tendremos en nuestra consola:

```python
http://0.0.0.0:8080/
```
Esta URL significa que el servidor esta escuchando todas las interfaces de red disponibles en el puerto 8080.

Pero la IP es designada por el sistema operativo o el contenedor.

## 1.8 Aplicación en funcionamiento

Al acceder a nuestro sitio web, en caso, el no se nos muestra nada, ya que nuestra ruta donde se encuentra el Index es /hola, por lo tanto para acceder hay que agregar esta dirección al la URL.

![Screenshot1](/aplicaciones_web/aplicacion01/screenshot1.png)

En la imagen se muestra que después de la URL usamos la ruta de nuestro **Index**, en este caso **/hola**

## 1.9 Detener el servidor
Para detener nuestra pagina web, dentro de la consola usaremos las teclas *Ctrl + C*, esta conbinacion detendra el servidor web

*Nota: Bajo ninguna circunstancia intente detener el servidor con las teclas *Ctrl + Z*, pues esto hara que pase a un segundo plano, impidiendole terminar o iniciar una nueva pagina web.*