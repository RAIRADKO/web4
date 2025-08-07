from flask import Blueprint, render_template, redirect, url_for, session

# Menghapus 'request' karena tidak lagi digunakan di sini
admin = Blueprint('admin', __name__, template_folder='templates')

# Fungsi login dihapus dari sini untuk menghindari konflik

@admin.route('/dashboard')
def dashboard():
    # Pemeriksaan sesi tetap dilakukan untuk melindungi rute ini
    if 'user' not in session:
        # Mengarahkan ke 'main.login' yang sekarang menjadi satu-satunya rute login
        return redirect(url_for('main.login'))
    return render_template('admin/dashboard.html')

@admin.route('/logout')
def logout():
    session.pop('user', None)
    # Mengarahkan ke 'main.login' setelah logout
    return redirect(url_for('main.login'))