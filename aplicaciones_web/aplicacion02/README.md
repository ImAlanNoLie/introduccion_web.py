# 2. Templates

## 2.1 Ejemplo de templates

Este codigo es un ejemplo del uso de templates HTML.

Más informacion en [Templetor web.py](https://webpy.org/docs/0.3/templetor)

Anteriormente en la [Aplicacion 01](/aplicaciones_web/aplicacion01/README.md), el codigo regresaba un texto plano "Hola mundo HTML y Python", pero en este caso devolvera un renderizado de un HTML.

```python
import web

urls = (
    '/', 'Index'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
```
## 2.2 Configurar tamplates

Primero hay que crear un objeto del tipo **web.template.render**, dentro hay que indicar el nombre de la carpeta, en este caso es 'templates', donde se almacenaran archivos **.html**, para posteriormente renderizarlos.

```python
render = web.template.render('templates')
```

## 2.3 Crear index.html

Ahora dentro de la carpeta hay que crear un archivo **index.html**, dentro de el colocaremos nuestro codigo en HTML, en este caso se uso el ejemplo proporcionado por [boostrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/).

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Hola mundo web.py</title>
</head>
<body>
    <h1>Hola mundo HTML y Python</h1>
    
</body>
</html>
```
## 2.4 Renderizado HTML

Esta vez en ves de texto plano, se llama a la clase **Index**, para que el método **GET** pueda renderizar el **index.html**.

```python
class Index:
    def GET(self):
        return render.index()
```

Una vez ejecutado se veria algo asi:

![Renderizado1](/aplicaciones_web/aplicacion02/screenshot1.png)

Si usamos la opción de inspeccionar en nuestro navegador, podremos comprobar que el codigo HTML pertenece al del archivo **index.html**:

![Renderizado2](/aplicaciones_web/aplicacion02/screenshot2.png)

