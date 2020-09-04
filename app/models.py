from app import db


class Test(db.Model):
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<User {}>'.format(self.id)

