from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display', methods=['POST'])
def display_file():
    file = request.files.get('file')  # Obtém o arquivo enviado.

    if not file or file.filename == '':
        return "Nenhum arquivo enviado", 400  # Retorna erro 400 se nenhum arquivo for enviado.

    # Verifica se o arquivo tem extensão .csv
    if not file.filename.endswith('.csv'):
        return "Apenas arquivos CSV são permitidos", 400

    # Tenta ler o arquivo CSV com diferentes codificações.
    try:
        df = pd.read_csv(file, sep=None, engine="python")  # Detecta automaticamente o delimitador.
    except UnicodeDecodeError:
        file.seek(0)
        try:
            df = pd.read_csv(file, encoding='latin1', sep=None, engine="python")
        except UnicodeDecodeError:
            file.seek(0)
            df = pd.read_csv(file, encoding='ISO-8859-1', sep=None, engine="python")

    return render_template('display.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask.