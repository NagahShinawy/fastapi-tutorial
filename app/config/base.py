import os
from pathlib import Path


API_V1_STR = "/api/v1"
API_V2_STR = "/api/v2"

PROJECT_NAME = "fastapi-ref"
OPENAPI_URL = os.getenv("OPENAPI_URL", f"/fastapi-ref{API_V1_STR}/openapi.json")
BASE_DIR = Path(".").absolute()

PORT = 8080

LOG_FORMAT = "<green>{time:YYYY-MMMM-DD HH:mm:ss}</green> | <red>{level}</red> | <level><yellow>{message}</yellow></level>"
