from flask import Flask # importar a 

server = Flask(__name__)

@server.route('/')

def root():
    return'<h1>Hello Word</h1>'

if __name__ == '__main__':
    server.run()