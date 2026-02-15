import reflex as rx

config = rx.Config(
    app_name="grc_platform",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    frontend_port=3000,
    backend_port=8001,
    api_url="https://risk-control-lab.preview.emergentagent.com:8001",
)
