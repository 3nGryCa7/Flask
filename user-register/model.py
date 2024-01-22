from register import db

class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(80), unique=True, nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(120), nullable=False)

    def __repr__(self):
        return 'Name: %r \nEmail: %r' % (self.name, self.email)