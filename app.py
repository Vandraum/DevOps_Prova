from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_directory, 'templates', 'index.html')

    if os.path.exists(index_path):
        return render_template('index.html')
    else:
        return "Erro: arquivo 'index.html' não encontrado."

if __name__ == '__main__':
    app.run(debug=True)
