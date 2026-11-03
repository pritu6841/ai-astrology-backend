import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "AI Astrology Backend"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    APP_ENV = os.getenv(
        "APP_ENV",
        "development"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "false"
    ).lower() == "true"

    API_V1_PREFIX = os.getenv(
        "API_V1_PREFIX",
        "/api/v1"
    )


settings = Settings()