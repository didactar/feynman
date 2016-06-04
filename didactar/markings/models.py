from database import db


class Marking(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

    def __init__(self, data):
        self.event_id = data.get('event').get('id')
        self.topic_id = data.get('topic').get('id')

    @classmethod
    def get_by_id(self, id):
        return Marking.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
