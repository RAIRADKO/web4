from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# Perubahan 1: Tambahkan 'template_folder' ke definisi Blueprint.
# Ini memberi tahu Flask untuk mencari template di dalam folder 'app/public/templates/'.
main = Blueprint('main', __name__, template_folder='public/templates')

# Perubahan 2: Tambahkan 'public/' di depan nama file template.
@main.route('/')
def index():
    try:
        # Flask sekarang akan mencari file di 'app/public/templates/public/index.html'
        return render_template('public/index.html')
    except TemplateNotFound:
        abort(404)

# Perubahan 3 (Opsional, tetapi praktik yang baik):
# Lakukan hal yang sama untuk rute lain jika ada.
# Contoh: Jika Anda memiliki halaman 'about.html'.
@main.route('/about')
def about():
    try:
        return render_template('public/about.html')
    except TemplateNotFound:
        abort(404)