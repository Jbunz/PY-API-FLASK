import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://localhost/ballpy")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

