import os
import mysql.connector
from flask import (Flask, redirect, url_for, session, 
                   request, render_template)
from werkzeug.security import check_password_hash

# Impor blueprint 'main' dari file routes.py
from app.routes import main as main_blueprint

def create_app():
    """Membungkus pembuatan aplikasi dalam sebuah fungsi (pola umum di Flask)."""
    app = Flask(__name__)
    app.secret_key = 'ganti-dengan-kunci-rahasia-yang-kuat-dan-unik'

    # --- Konfigurasi Koneksi MySQL ---
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'  # Ganti dengan username MySQL Anda
    app.config['MYSQL_PASSWORD'] = '' # Ganti dengan password MySQL Anda
    app.config['MYSQL_DB'] = 'website_kominfo' # Pastikan nama database ini sudah ada
    app.config['UPLOAD_FOLDER'] = 'static/favicon'
    
    # Membuat folder upload jika belum ada
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    def get_db():
        """Fungsi helper untuk membuat koneksi ke database MySQL."""
        return mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )

    # --- Rute untuk Admin dan Autentikasi ---
    @main.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password_input = request.form['password']
            
            conn = get_db()
            cursor = conn.cursor(dictionary=True) # dictionary=True agar hasil bisa diakses per kolom
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user and check_password_hash(user['password'], password_input):
                session['user'] = user['username']
                return redirect(url_for('dashboard'))
            else:
                return "Login Gagal. Periksa kembali username dan password Anda.", 401
        return render_template('admin/login.html')

    @main.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('login'))
        
    @main.route('/dashboard')
    def dashboard():
        if 'user' not in session:
            return redirect(url_for('login'))
        return render_template('admin/dashboard.html')

    @main.route('/identitas', methods=['GET', 'POST'])
    def identitas():
        if 'user' not in session:
            return redirect(url_for('login'))
        
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        if request.method == 'POST':
            data = request.form
            file = request.files.get('favicon')
            favicon_name = data.get('old_favicon')
            
            if file and file.filename:
                favicon_name = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], favicon_name))

            sql = """
                UPDATE identitas_website SET
                  nama_website=%s, email=%s, domain=%s, sosial_network=%s,
                  no_rekening=%s, no_telpon=%s, meta_deskripsi=%s, meta_keyword=%s,
                  Maps=%s, favicon=%s
                WHERE id=1
            """
            values = (
                data['nama_website'], data['email'], data['domain'], data['sosial_network'],
                data['no_rekening'], data['no_telpon'], data['meta_deskripsi'], data['meta_keyword'],
                data['Maps'], favicon_name
            )
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('identitas'))

        cursor.execute('SELECT * FROM identitas_website WHERE id=1')
        identitas_data = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('admin/identitas_website.html', data=identitas_data)

    # --- Daftarkan Blueprint dari routes.py ---
    # Ini memberitahu aplikasi utama untuk menggunakan semua rute yang ada di file routes.py
    app.register_blueprint(main_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)