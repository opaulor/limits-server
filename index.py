from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa a extensão flask-cors
from sympy import symbols, limit, sympify

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Habilita o CORS e define métodos permitidos
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/calcular_limite', methods=['POST'])
def calcular_limite():
    # Recebe os dados JSON do frontend
    dados = request.get_json()

    # Extrai a expressão, a variável e o ponto de limite dos dados recebidos
    expressao = dados.get('expressao', '')
    variavel = dados.get('variavel', 'x')
    ponto = dados.get('ponto', 0)

    try:
        # Cria o símbolo para a variável
        x = symbols(variavel)

        # Converte a expressão em uma expressão do SymPy
        expr = sympify(expressao)

        # Calcula o limite da expressão no ponto dado
        resultado = limit(expr, x, ponto)

        # Retorna o resultado em formato JSON
        return jsonify({'resultado': str(resultado)}), 200  # Garante status HTTP 200 OK

    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
