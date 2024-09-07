from flask import Flask, render_template, redirect,  url_for, flash, request, session
from parameters import params

app = Flask(__name__)
app.secret_key = params.app_secret_key


@app.route('/')
def loginpage():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    
    username = request.form['username']
    password = request.form['password']
    
    if username == params.USERNAME and password == params.PASSWORD:
        
        session['logged_in'] = True
        return redirect(url_for('index'))
    
    else:
        
        flash('Il nome utente o la password sono errati')
        
        return redirect(url_for('loginpage'))


@app.route('/protected')
def index():
    
    if not session.get('logged_in'):
        
        return redirect(url_for('loginpage'))

    posts = params.database.get_posts()

    return render_template('index.html', posts=posts)


@app.route('/logout')
def logout():
    
    session.pop('logged_in', None)  # Usa pop per rimuovere la chiave
    
    return redirect(url_for('loginpage'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):

    params.database.delete_post(id)

    return redirect('/protected')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        titolo = request.form.get('titolo')
        spiegazione = request.form.get('spiegazione')

        params.database.add_post(titolo, spiegazione)

        return redirect('/protected')
    return render_template('create.html')
