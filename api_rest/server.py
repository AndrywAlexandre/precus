from flask import Flask
from app import create_app  # Importa a factory function

app = create_app()  # Cria a instância da aplicação

if __name__ == '__main__':
    app.run(debug=True)  # Executa em modo de desenvolvimento