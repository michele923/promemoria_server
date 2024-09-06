from flask import Flask, render_template, redirect, request, url_for, session, flash
import sqlite3



app = Flask(__name__)
app.secret_key = '12345678'  # chiave segreta per gestire le sessioni
USERNAME = 'michele923'
PASSWORD = 'prusamk3s+'

@app.route('/')
def loginpage():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        session['logged_in'] = True
        return redirect(url_for('index'))
    else:
        flash('Il nome utente o la password sono errati')
        return redirect(url_for('loginpage'))

@app.route('/protected')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('loginpage'))
    connection = sqlite3.connect('db.db')
    connection.row_factory = sqlite3.Row
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Usa pop per rimuovere la chiave
    return redirect(url_for('loginpage'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    connection = sqlite3.connect('db.db')
    connection.row_factory = sqlite3.Row
    connection.execute('DELETE FROM posts WHERE id=?', (id,))
    connection.commit()
    connection.close()
    return redirect('/protected')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        titolo = request.form.get('titolo')
        spiegazione = request.form.get('spiegazione')  # Assicurati che il nome sia 'spiegazione'
        connection = sqlite3.connect('db.db')
        connection.row_factory = sqlite3.Row
        connection.execute('INSERT INTO posts(titolo, spiegazione) VALUES (?,?)', (titolo, spiegazione))  # Usa 'spiegazione'
        connection.commit()
        connection.close()
        return redirect('/protected')
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
