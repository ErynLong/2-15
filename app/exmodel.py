# from app import db
# class Pokemon(db.Model):
#     # __tablename__ = 'pokemon'
#     poke_id = db.Column(db.Integer, primary_key=True)
#     #this field [name] should probably be unique since we will be using this to look up pokemon
#     name = db.Column(db.String) 
#     hp = db.Column(db.Integer)

# class PokemonPokeMaster(db.Model):
#     poke_id = db.Column(db.Integer, db.ForeignKey('pokemon.poke_id'), primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('poke_master.user_id'), primary_key=True)

# class PokeMaster(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     pokemen = db.relationship('Pokemon',
#                     secondary = 'pokemon_poke_master',
#                     backref='users',
#                     lazy='dynamic',
#                     # cascade="all, delete-orphan"  how you would do on cascade delete if you wanted it
#                     )

#     def collect_poke(self, poke):
#         self.pokemen.append(poke)
#         db.session.commit()
        


