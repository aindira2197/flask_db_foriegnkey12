from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    accounts = db.relationship('Account', backref='customer', cascade="all, delete")


class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)

    number = db.Column(db.String(30))
    balance = db.Column(db.Float)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'))

    transactions = db.relationship('Transaction', backref='account', cascade="all, delete")


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float)
    type = db.Column(db.String(20))  # deposit/withdraw

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id', ondelete='CASCADE'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


menga shunaqa 100 foiz toliq qilib 5 ta masala yozib ber
