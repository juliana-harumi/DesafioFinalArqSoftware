from flask import Flask
from model.domains.produto import db
from control.produto_controller import produto_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(produto_bp)

if __name__ == '__main__':
    app.run(debug=True)