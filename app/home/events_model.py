from app import db


class ScheduledEvents(db.Model):
    """[summary]

    Args:
        db ([type]): [description]
    """

    __tablename__ = "scheduled_events"
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    desc = db.Column(db.String)
    date = db.Column(db.DateTime)
    img = db.Column(db.String)
    active = db.Column(db.Boolean)
