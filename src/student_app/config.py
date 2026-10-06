import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv(*args, **kwargs):
        return False


load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Student App")
DEBUG = str(os.getenv("DEBUG", "False")).strip().lower() == "true"
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "100"))
API_KEY = os.getenv("API_KEY")