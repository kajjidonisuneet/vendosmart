from xml.etree.ElementInclude import include
from app import db

class Vendor (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    location = db.Column(db.String(128), index=True, nullable=False)
    rating = db.Column(db.Integer, index=True, nullable=False)
    skills = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"Vendor data id:{self.id}, name:{self.name}, location:{self.location}, rating:{self.rating}, skill:{self.skills}"

    def from_dict(self, data):
        for field in ['name', 'location', 'rating', 'skills']:
            if field in data and data[field] != None:
                setattr(self, field, data[field])

    def to_dict(self, include_id=False):
        data = {
            "Company_name": self.name,
            "Location": self.location,
            "Skills": self.skills,
            "Rating": self.rating
        }
        
        if include_id:
            data['id'] = self.id

        return data
    
    @staticmethod
    def to_collection(items):
        data = [ item.to_dict() for item in items]
        data.append (f'total number of matched vendors: {len(items)}')
        return data