# Importação do servidor,
# método para retornar JSON e controlador dos dados.
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "O Senhor dos Pasteis - As Duas Fomes",
        "autor": "Leonardo Maieski"
    },
    {
        "id": 2,
        "titulo": "Harry Porco: As Relíquias da Roça",
        "autor": "Lyla Stanichesck"
    },
    {
        "id": 3,
        "titulo": "Usuário: Manual do Usuário",
        "autor": "Kaike Olodum"
    }
]

# GET ------------
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)

# GET (id) ------------
@app.route("/livros/<int:id>", methods=["GET"])
def obter_livro_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)

# POST
@app.route("/livros", methods=["POST"])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# PUT ------------
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro(id):
    livro_alterado = request.get_json()
    for index, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[index].update(livro_alterado)
            return jsonify(livros[index])

# DELETE ------------
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir(id):
    for index, livro in enumerate(livros):
        if livro.get("id") == id:
            del livros[index]
            return jsonify(livros)

# Executar app
app.run(host="localhost", port=5000, debug=True)
