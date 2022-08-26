from app import db

class Vendor (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    location = db.Column(db.String(128), index=True, nullable=False)
    rating = db.Column(db.Integer, index=True, nullable=False)
    skill = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"Vendor data id:{self.id}, name:{self.name}, location:{self.location}, rating:{self.rating}, skill:{self.skill}"