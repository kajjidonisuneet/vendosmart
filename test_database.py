
from app import Vendor
from app import db

v = Vendor(name='Suneet', location='pune', skill='coding', rating=5)

db.session.add(v)
db.session.commit()

