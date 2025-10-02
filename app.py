from flask import Flask, jsonify, request
from database import db
from controllers.refeicao import RefeicaoController


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:admin123@localhost:3307/flask_db"
db.init_app(app)


@app.route("/refeicao", methods=["POST"])
def create_refeicao(): 
    data = request.json 
    nome = data.get("nome")
    descricao = data.get("descricao")
    data_hora = data.get("data_hora")
    esta_na_receita = data.get("esta_na_receita")
   
    if nome and descricao and data_hora and esta_na_receita:
        refeicao = RefeicaoController(nome=nome, descricao=descricao, data_hora=data_hora, esta_na_receita=esta_na_receita)
        db.session.add(refeicao)
        db.session.commit()
        return jsonify({"message": "Refeicao criada com sucesso"}), 201
    else:
        return jsonify({"message": "Dados incompletos"}), 400

@app.route("/refeicao/<int:id>", methods=["PUT"])
def update_refeicao(id): 
    data = request.json 
    refeicao = RefeicaoController.query.get(id)

    if data.get("nome"):
        refeicao.nome = data.get("nome")
    if data.get("descricao"):
        refeicao.descricao = data.get("descricao")
    if data.get("data_hora"):
        refeicao.data_hora = data.get("data_hora")
    if data.get("esta_na_receita") is not None:
        refeicao.esta_na_receita = data.get("esta_na_receita")
    
    db.session.commit()
    return jsonify({"message": "Refeicao atualizada com sucesso"}), 200


@app.route("/refeicao/<int:id>", methods=["DELETE"])
def delete_refeicao(id):
    refeicao = RefeicaoController.query.get(id)
    db.session.delete(refeicao)
    db.session.commit()
    return jsonify({"message": "Refeicao deletada com sucesso"}), 200


@app.route("/refeicao", methods=["GET"])
def listar_refeicoes():
    refeicoes = RefeicaoController.query.all()
    return jsonify({"refeicoes": [refeicao.to_dict() for refeicao in refeicoes]}), 200


@app.route("/refeicao/<int:id>", methods=["GET"])
def get_refeicao(id):
    refeicao = RefeicaoController.query.get(id)
    return jsonify({"refeicao": refeicao.to_dict()}), 200

if __name__ == "__main__":
    app.run(debug=True, port=3000)