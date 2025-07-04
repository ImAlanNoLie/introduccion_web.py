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

        try:
            numero1 = int(formulario.inp_numero1)
            numero2 = int(formulario["inp_numero2"])
        except ValueError:
            return render.calculadora("Error",0,0)
    
        operacion = formulario.btn_operation

        if operacion == "suma":
            resultado = numero1 + numero2
        elif operacion == "resta":
            resultado = numero1 - numero2
        elif operacion == "multiplicacion":
            resultado = numero1 * numero2
        elif operacion == "division":
            if numero2 == 0:
                resultado = "Error: Por favor, ingresa un número valido"
            else:
                resultado = numero1 / numero2

        return render.calculadora(resultado, numero1, numero2)

if __name__ == "__main__":
    app.run()

    