import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

class Settings:
    def __init__(self):
        self.API_TIMEOUT = 30  # seconds
        self.LOG_LEVEL = logging.INFO
        self.MAX_RETRIES = 3

settings = Settings()