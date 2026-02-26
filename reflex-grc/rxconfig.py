import reflex as rx
import os

BACKEND_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://control-center-66.preview.emergentagent.com")

config = rx.Config(
    app_name="grc_platform",
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,
    frontend_port=3000,
    backend_port=8001,
    api_url=f"{BACKEND_URL}/api",
)
