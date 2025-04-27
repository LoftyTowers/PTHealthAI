import os

class Config:
    # Database connection URI
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:yourpassword@db:5432/pthealthai"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask specific config (optional future)
    DEBUG = os.getenv("DEBUG", "True") == "True"
