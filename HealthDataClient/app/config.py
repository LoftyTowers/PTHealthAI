import os

class Config:
    # URLs of internal services (DatabaseService)
    DATABASESERVICE_URL = os.getenv(
        "DATABASESERVICE_URL",
        "http://databaseservice:5001"
    )

    # Example external API keys (for future third-party API integrations)
    GARMIN_API_KEY = os.getenv("GARMIN_API_KEY", "your-garmin-api-key")
    STRAVA_API_KEY = os.getenv("STRAVA_API_KEY", "your-strava-api-key")
    OURA_API_KEY = os.getenv("OURA_API_KEY", "your-oura-api-key")

    # Flask specific config (optional future)
    DEBUG = os.getenv("DEBUG", "True") == "True"
