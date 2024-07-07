from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':        
        username = request.form['username']
        password = request.form['password']
        # Exemplo simples de validação
        if username == 'admin' and password == 'admin':
            return redirect(url_for('home'))
        else:
            return "Credenciais Inválidas!"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
