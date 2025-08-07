from flask import Flask
from app.routes import main as main_blueprint
from app.admin.routes import admin as admin_blueprint

def create_app():
    app = Flask(__name__)
    app.secret_key = 'rahasia-banget'

    # Daftarkan semua blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)

    return app
