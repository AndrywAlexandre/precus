import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

class Config:
    # Chave secreta para segurança das sessões do Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
    
    # URL de conexão com o PostgreSQL (formato: postgresql://user:password@host/database)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    # Desativa rastreamento de modificações para melhor performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False