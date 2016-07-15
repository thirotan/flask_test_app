from first_app import db

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} comment={comment}>'.format(id=self.id, comment=self.comment)

def init():
    db.create_all()
