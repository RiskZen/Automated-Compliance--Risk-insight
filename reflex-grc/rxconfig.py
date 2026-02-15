import reflex as rx

config = rx.Config(
    app_name="grc_platform",
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,
    frontend_port=3000,
    backend_port=3000,
)
