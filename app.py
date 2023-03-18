from flask import Flask, render_template
from flask import request

from forms2 import PalabraForm
from Rforms import ResistForm
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import make_response
from resistencia import ColorResistencia

app=Flask(__name__)
app.config['SECRET_KEY'] = "Clave Encriptada"
csrf = CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template("404.html"),404

@app.route("/diccionario", methods = ["GET", "POST"])
def diccionario():
    speak_form = PalabraForm(request.form)
    Eng = ""
    Sph = ""
    Dicc = {}

    if request.method=="POST":

        Eng = speak_form.ingles.data
        Sph = speak_form.espaniol.data
        print(Sph)
        print(Eng)

        Dicc = {Eng.lower():Sph.lower()}
        print(Dicc)

        with open("datos.txt", "a") as f:
            for palabraEn, palabraEs in Dicc.items():
                f.write("{}:{}\n".format(palabraEn, palabraEs))
        
        
    return render_template("Actividad2.html", form=speak_form)


@app.route("/palabra2", methods = ["GET", "POST"])
def traduccion():
    speak_form = PalabraForm(request.form)

    palabra = ""
    palabras = {}
    encontrado = False

    if request.method=="POST":
        palabra = speak_form.palabra.data
        with open("datos.txt","r") as archivo:
             for linea in archivo:
                palabraEn, palabraEs = linea.strip().split(":")
                palabras[palabraEn.lower()]=palabraEs.lower()
                print(palabras)
                
                
           

        if request.form.get("idioma") == "ingles":
            for palabraEn,palabraEs in palabras.items():
                if palabraEs == palabra.lower():
                    print(palabraEn)
                    encontrado = True
                    return render_template("Actividad2.html", form=speak_form, palabra=palabraEn)
            if not encontrado:
                    return render_template("Actividad2.html", form=speak_form, palabra="No existe")
                
            return
        if request.form.get("idioma") == "espaniol":
            for palabraEn,palabraEs in palabras.items():
                if palabraEn == palabra.lower():
                    print(palabraEs)
                    encontrado = True
                    return render_template("Actividad2.html", form=speak_form, palabra=palabraEs)
            if not encontrado:
                return render_template("Actividad2.html", form=speak_form, palabra="No existe")
            
@app.route("/resistencia", methods=["GET","POST"])
def resistencia():

    rforms = ResistForm()
    valor_cookie=request.cookies.get("datos_user")
    Nombre = valor_cookie.split("@")
    e1 = 0
    e2 = 0
    e3 = 0
    tol = 0
    cb1 = " "
    cb2 = " "
    cb3 = " "
    ctol = " "
    valor = 0 
    max = 0 
    mini = 0
    backg1 = " "
    backg2 = " "
    backg3 = " "
    backg4 = " "

    textco1 = " "
    textco2 = " "
    textco3 = " "
    
    

    if request.method=="POST" and Nombre != None:
       e1 = int(request.form["banda1"])
       e2 = int(request.form["banda2"])
       e3 = int(request.form["banda3"])
       tol = float(request.form.get("rbtnTol"))

       print("banda 1: {}, banda 2: {}, banda 3: {}, tol: {}".format(e1,e2,e3, tol))

       print("min: {}, ohms: {}, max: {}".format((((e1+e2)*e3)*(tol+1)),((e1+e2)*e3),(((e1+e2)*e3)-(((e1+e2)*e3)*tol))))

       valor = (e1+e2)*e3
       max = ((e1+e2)*e3)*(tol+1)
       mini = ((e1+e2)*e3)-(((e1+e2)*e3)*tol)
       

       colors = ColorResistencia(e1, e2, e3, tol)    
       cb1 = colors.banda1()
       cb2 = colors.banda2()
       cb3 = colors.banda3()
       ctol = colors.tolerancia()

       backg1 = colors.color1()
       backg2 = colors.color2()
       backg3 = colors.color3()
       backg4 = colors.color4()

       #textco1 = colors.text1()
       #textco2 = colors.text2()
       #textco3 = colors.text3()

       print("{}, {}, {}, {}".format(cb1,cb2,cb3,ctol))

       

    return render_template("Resistencias.html", form=rforms, banda_1=cb1, banda_2=cb2, banda_3=cb3, tolerancia=ctol, valor=valor, mini=mini, max=max, nom=Nombre[0], bgc1=backg1, bgc2=backg2, bgc3=backg3,
                           bgc4=backg4)
                
        

if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)