import sqlalchemy as db


class HasReportConsensus:
    """When a descriptive item on a fungus is tagged with a value,
     this value is incremented, when removed, decremented. This allows
     for sorting to determine the most common traits, as well as removing false traits.
     For example, if a fungus is tagged as associating with pine trees more often than oak,
     the consensus for pine would be higher."""
    report_consensus = db.Column(db.Integer, default=1, nullable=False)


class TagTable:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
