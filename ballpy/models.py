from ballpy import db

class Reptile(db.Model):
    __tablename__ = "reptiles"

    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(100), nullable=False)
    conservation_status = db.Column(db.String(100), nullable=False)
    native_habitat = db.Column(db.String(255), nullable=False)
    fun_fact = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "common_name": self.common_name,
            "scientific_name": self.scientific_name,
            "conservation_status": self.conservation_status,
            "native_habitat": self.native_habitat,
            "fun_fact": self.fun_fact
        }
