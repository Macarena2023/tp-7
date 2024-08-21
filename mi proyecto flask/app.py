from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
 return render_template('home.html')


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
 if request.method == 'POST':
  nombre = request.form.get('nombre')
  mensaje = request.form.get('mensaje')

  return f"Gracias {nombre}, hemos recibido tu mensaje: {mensaje}"

 return render_template('contacto.html')

@app.route('/perfil/<nombre>')
def perfil(nombre):
  return render_template('perfil.html', nombre=nombre)

if __name__ == '__main__':
 app.run(debug=True)