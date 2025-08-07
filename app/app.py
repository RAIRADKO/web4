import os
import mysql.connector
from flask import (Flask, redirect, url_for, session,
                   request, render_template)
from werkzeug.security import check_password_hash, generate_password_hash

# Impor blueprint 'main' dan 'admin'
from app.routes import main as main_blueprint
from app.admin.routes import admin as admin_blueprint

def create_app():
    """Membungkus pembuatan aplikasi dalam sebuah fungsi."""
    app = Flask(__name__)
    app.secret_key = 'ganti-dengan-kunci-rahasia-yang-kuat-dan-unik'

    # --- Konfigurasi Koneksi MySQL ---
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'web_kominfo'
    app.config['UPLOAD_FOLDER'] = 'static/favicon'

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    def get_db():
        """Fungsi helper untuk koneksi ke database MySQL."""
        return mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )

    # --- Rute Autentikasi Terpusat ---
    # Rute login ini sekarang akan diakses melalui blueprint 'main'
    @main_blueprint.route('/login', methods=['GET', 'POST'])
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

            # Memeriksa apakah user ada dan password hash-nya cocok
            if user and check_password_hash(user['password'], password_input):
                session['user'] = user['username']
                # Mengarahkan ke dashboard admin setelah berhasil login
                return redirect(url_for('admin.dashboard'))
            else:
                return "Login Gagal. Periksa kembali username dan password Anda.", 401
        return render_template('admin/login.html')

    # --- Daftarkan Blueprint ---
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin') # Menambahkan prefix untuk rute admin

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)