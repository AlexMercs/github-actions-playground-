from flask import Flask


def create_app():
    app = Flask(__name__)

    # Basic config (you can expand later)
    app.config["SECRET_KEY"] = "dev"

    # Import and register routes
    from app.routes import main
    app.register_blueprint(main)

    return app


# For simple usage (like tests)
app = create_app() 
