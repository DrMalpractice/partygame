from flask import render_template, request, session, redirect, url_for, g
from partygame import app
from db import connect_db
import partygame.auth
import os

@app.before_request
def before_request():
    g.db = connect_db()
    
@app.teardown_request
def teardown_request(exception):
    g.db.close()
    
@app.route('/')
def home():
    return render_template('home.html', user=session.get('user', None))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session and session['user']:
            return redirect(url_for('home'))
        else:
            return render_template('loginform.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = partygame.auth.login(g.db, username, password)
        if user:
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return render_template('loginform.html', error='Incorrect username/password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'user' in session and session['user']:
            return redirect(url_for('home'))
        else:
            return render_template('registerform.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        email = request.form['email']
        
        cursor = g.db.cursor()
        numusers = cursor.execute('select count(*) from user where username=?', [username]).fetchone()[0]
        numemails = cursor.execute('select count(*) from user where email=?', [email]).fetchone()[0]
        
        errors = []
        if len(username) > 20 or len(username) < 3:
            errors.append('Username must be between 3 and 20 characters long')
        if not all(i.isalnum() or i == '_' for i in username):
            errors.append('Username can only contain alpahnumeric characters and underscores')
        if numusers > 0:
            errors.append('That username is already in use, usernames must be unique')
        if len(password) < 6:
            errors.append('Password must be at least 6 characters long')
        if password != password2:
            errors.append('Passwords must match')
        if '@' not in email or '.' not in email or len(email) < 8:
            errors.append('A valid email address is required')
        if numemails > 0:
            errors.append('That email address is already in use, email addresses must be unique')
        
        if errors:
            return render_template('registerform.html', errors=errors)
        else:
            user = partygame.auth.create_user(g.db, username, password, email)
            if user:
                g.db.commit()
                session['user'] = user
                return redirect(url_for('home'))
            else:
                return render_template('registerform.html', errors=['Unknown error creating user'])
            
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('home'))
