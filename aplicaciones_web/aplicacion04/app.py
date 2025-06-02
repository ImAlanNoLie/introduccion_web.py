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