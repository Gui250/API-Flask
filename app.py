from flask import Flask, jsonify, request
from database import db
from controllers.refeicao import RefeicaoController


app = Flask(__name__)
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



if __name__ == "__main__":
    app.run(debug=True, port=3000)