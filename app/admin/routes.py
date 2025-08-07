from flask import Blueprint, render_template, request, redirect, url_for, session

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/login', methods=['GET', 'POST'])
def login():
    # Logika login sederhana (bisa kamu sambungkan ke database juga)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['user'] = username
            return redirect(url_for('admin.dashboard'))
        else:
            return "Login gagal", 401
    return render_template('admin/login.html')

@admin.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('admin.login'))
    return render_template('admin/dashboard.html')

@admin.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('admin.login'))
