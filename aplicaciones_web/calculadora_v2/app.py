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

        numero1 = int(formulario.inp_numero1)
        numero2 = int(formulario["inp_numero2"])
        operacion = formulario.btn_operation

        if operacion == "suma":
            resultado = numero1 + numero2
        elif operacion == "resta":
            resultado = numero1 - numero2
        elif operacion == "multiplicacion":
            resultado = numero1 * numero2
        elif operacion == "division" and numero2 != 0:
            resultado = numero1 / numero2
        else:
            resultado = "Ingresa un número valido"
            
        return render.calculadora(resultado)

if __name__ == "__main__":
    app.run()

    