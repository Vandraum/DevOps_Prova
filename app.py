from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def Home_Page():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    index_path = os.path.join(current_directory, 'index.html')

    if os.path.exists(index_path):
        with open(index_path, 'r') as file:
            content = file.read()
        return content
    else:
        return "Erro: arquivo 'index.html' não encontrado."

if __name__ == '__main__':
    app.run()
