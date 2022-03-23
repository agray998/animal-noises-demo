from application import db

class Results(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.String(10))
    noise = db.Column(db.String(10))
    def __str__(self):
        return f"{self.animal} goes {self.noise}"