import web

urls = (
    '/', 'Calculadora'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Calculadora:

    def GET(self):
        return render.calculadora()
    
    def POST(self):
        formulario = web.input()
        print(formulario)

        numero1 = int(formulario.inp_numero1)
        numero2 = int(formulario["inp_numero2"])

        resultado = numero1 + numero2
        return render.calculadora(resultado)

if __name__ == "__main__":
    app.run()

    