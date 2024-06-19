from flask import Flask, render_template 
 
app = Flask (__name__)
 
@app.route('/')
def base():
    return render_template('base.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/certificacoes')
def certificacoes():
    return render_template('certificacoes.html')
 
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/contatos')
def projetos():
    return render_template('contatos.html')

@app.route('/sobremim')
def projetos():
    return render_template('sobremim.html')
 
 
if __name__ == '__main__':
    app.run(debug=True)