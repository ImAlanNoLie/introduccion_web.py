# 4. Navegar entre paginas

## 4.1 Ejemplo con Templates

En la [Aplicación 4](/aplicaciones_web/aplicacion03/README.md) aprendimos a usar datos de Python en HTML, el objetivo de esta aplicación es lograr navegar entre paginas dentro de la misma web.

```python
import web

urls = (
    '/', 'Index',
    '/bienvenida','Bienvenida'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Index:

    def __init__(self):
        self.mensaje = "Este es un texto cualquiera"

    def GET(self):
        return render.index(self.mensaje)
    
class Bienvenida:

    def __init__(self):
        pass

    def GET(self):
        mensaje = "Esta es la bienvenida"
        return render.bienvenida(mensaje)


if __name__ == "__main__":
    app.run()
```
Uno de los principales cambios dentro del codigo de esta aplicación es la generación de dos rutas, estas representan la ruta de las paginas dentro de nuestra web.

```python
urls = (
    '/', 'Index',
    '/bienvenida','Bienvenida'
)
```

## 4.2 Paginas web

Como mencionamos anteriormente, usaremos dos paginas web:

- La primera de nombre **Index** con la ruta raiz **/**
- Una segunda pagina **Bienvenida** con la ruta **/bienvenida**

Posteriormente creamos sus respectivos archivos .html

idex.html
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
    <a href="/bienvenida">bienvenida</a>
  </body>
</html>
```

bienvenida.html
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
    <a href="/">Index</a>
  </body>
</html>
```

En ambos archivos .html hubo una línea nueva:

```html
<a href="/bienvenida">bienvenida</a>

<a href="/">Index</a>
```
Estas líneas son las responsables de crear enlaces dentro de una página web, dentro de **href** se coloca la URL de la página y lo que queda fuera sera el texto que permitira cambiar de pagina (algo como un boton).

## 4.3 Renderizar páginas

Dentro de nuestro codigo en python, crearemos las respectivas clases que corresponden para cada pagina web.

```python
class Index:

    def __init__(self):
        self.mensaje = "Este es un texto cualquiera"

    def GET(self):
        return render.index(self.mensaje)
    
class Bienvenida:

    def __init__(self):
        pass

    def GET(self):
        mensaje = "Esta es la bienvenida"
        return render.bienvenida(mensaje)
```

Aún tenemos nuestra variable global **mensaje**, ahora añadimos una segunda variable dentro del método GET de la clase Bienvenida, con un mensaje distinto.

Como ya sabemos, el método GET nos permite renderizar estas paginas web.

***Nota**: renderizar quiere decir que todo el codigo html, css o javascript, se convierta en la representacion visual que normalmente vemos en nuestro navegador.*

Por ultimo comprobamos:

![Screenshot1](/aplicaciones_web/aplicacion04/screenshot1.png)

Vemos que el boton para ir a la pagina bienvenida se encuentra ahi.

![Screenshot2](/aplicaciones_web/aplicacion04/screenshot2.png)

Comprobamos que la pagina **/bienvenida** funciona pues en la URL se nos muestra la dirección.