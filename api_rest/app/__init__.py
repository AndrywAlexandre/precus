from flask import Flask
from app.config import Config
from app.database import db

def create_app():
    app = Flask(__name__)
    
    # Carrega configurações do arquivo Config
    app.config.from_object(Config)
    
    # Inicializa o banco de dados com a aplicação
    db.init_app(app)
    
    # Registra Blueprints (módulos de rotas)
    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
