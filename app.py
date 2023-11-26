from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def Home_Page():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_directory, 'index.html')

    if os.path.exists(index_path):
        with open(index_path, 'r') as file:
            content = file.read()
        css_content = '<link rel="stylesheet" type="text/css" href="style.css">'
        
        content = css_content + content
        return content
    else:
        return "Erro: arquivo 'index.html' não encontrado."

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(current_directory, filename)


if __name__ == '__main__':
    app.run()

