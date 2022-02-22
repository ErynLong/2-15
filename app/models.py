from app import db, login
from flask_login import UserMixin # This is just for the User model!
from datetime import datetime as dt, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

class Cart(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def remove(self):
        db.session.delete(self)
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), index=True, unique=True)
    password = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, default = dt.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    user_cart = db.relationship('Item',
        secondary = 'cart',
        backref='user',
        lazy='dynamic')
    
    def __repr__(self):
        return f'<User: {self.id} | {self.email}>'

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    def save(self):
        db.session.add(self) 
        db.session.commit() 

    def add_to_user_cart(self, data):
        self.user_cart.append(data)
        self.save()
    
    def total(self):
        all_prices = []
        for item in self.user_cart:
            all_prices.append(item.price)
            final_total = sum(all_prices)
        return str(final_total)

    def delete_from_cart(self, data):
        self.user_cart.delete(data)
        self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.Text)
    price = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return f'<Post: {self.id} | {self.body[:15]}>'

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'body':self.body,  
            'price':self.price,
            'date_created':self.date_created,
        }

    def edit(self, new_body):
        self.body = new_body
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # saves the post to the database
    def save(self):
        db.session.add(self) # add the user to the db session
        db.session.commit() #save everything in the session to the database

