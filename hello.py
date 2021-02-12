from flask import Flask, render_template  
app = Flask(__name__) 

@app.route('/')
def diccionario():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html',users=users)
   
#@app.route('/4')         
#def tablero_4():
#    return render_template('index2.html')

#@app.route('/<numero>/<numero2>') 
#def tablero_personalizadp(numero,numero2):
#    return render_template('index3.html',filas=int(numero),columnas=int(numero2))

if __name__=="__main__":   
    app.run(debug=True) 