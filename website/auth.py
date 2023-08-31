from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    from .models import db
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            email = request.form.get('email')
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            
            new_user = User(username=username, password=hashed_password, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration.', category='error')
            flash(str(e), 'error')
            print(e)
    
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    from .models import db
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Attempting login with username: {email} and password: {password}")
        
        user = User.query.filter_by(email=email).first()
        print(f"User object retrieved: {user}")

        if user:
            if check_password_hash(user.password_hash, password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                print("Login successful")
                #return redirect(url_for('views.saved_recipes')) 'success')
                return redirect(url_for('views.index'))
            else:
             flash('Incorrect Password', category='error')
        else:
            flash('Email is not correct. Try Again', category='error')
            print("Invalid login attempt")
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))