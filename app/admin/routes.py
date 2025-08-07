from flask import Blueprint, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import check_password_hash

admin = Blueprint('admin', __name__, template_folder='templates')

def get_db():
    """Fungsi helper untuk koneksi ke database MySQL."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='web_kominfo'
    )

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_input = request.form['password']

        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user['password'], password_input):
            session['user'] = user['username']
            return redirect(url_for('admin.dashboard'))
        else:
            return "Login Gagal. Periksa kembali username dan password Anda.", 401
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