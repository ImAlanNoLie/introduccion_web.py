# 3. Templates y datos

## 3.1 Ejemplo de tamplates

Este codigo es un ejemplo del uso de templates HTML.

Más informacion en [Templetor web.py](https://webpy.org/docs/0.3/templetor)

Anteriormente en la [Aplicacion 02](/aplicaciones_web/aplicacion02/README.md) mediante la clase **Index** mandamos a llamar al método **GET** que permitio que renderizaramos un **index.html**.

```python
import web

urls = (
    '/', 'Index'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Index:

    def __init__(self):
        self.mensaje = "Este es un texto cualquiera"

    def GET(self):
        return render.index(self.mensaje)

if __name__ == "__main__":
    app.run()
```
## 3.2 Usar Python para enviar datos a HTML
Dentro de la clase **Index**, creamos un constructor mediante el método **init**, y aqui generamos una variable global.

*Nota: Una variable global es aquella que puede ser utilizada en cualquier parte de la clase, sin importar si se encuentra dentro de un método o no*

```python
def __init__(self):
    self.mensaje = "Este es un texto cualquiera"
```
Ahora pasamos al archivo **index.html**, y fuera del codigo HTML colocamos: **$def with(mensaje)**

```html
$def with(mensaje)
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>web.py</title>
  </head>
  <body>
    <h1>$mensaje</h1>
    <h2>"Hola"</h2>
  </body>
</html>
```

## 3.3 Renderizar variables
Los datos de python en HTML se reciben con **def with(mensaje)**, el simbolo **$** significa que va a ser renderizado, por lo tanto dentro del codigo, se mostrara el contenido de **$mensaje**.

```html
<h1>$mensaje</h1>
```

Contenido de **$mensaje**:

```python
def __init__(self):
        self.mensaje = "Este es un texto cualquiera"
```

## 3.4 Renderizar index.html
Ahora para lograr renderizar esta variable junto con el index, en python somos capaces de imprimir cualquier variable, por lo tanto lo colocamos dentro de método GET, que es el que renderiza el archivo.

```python
def GET(self):
    return render.index(self.mensaje)
```

Por ultimo revisamos los cambios:

![Screenshot1](/aplicaciones_web/aplicacion03/screenshot1.png)

Y comprobamos con el codigo HTML:

![Screenshot2](/aplicaciones_web/aplicacion03/screenshot2.png)

Como se menciono anteriormente, se renderiza el contenido de **$mensaje**.