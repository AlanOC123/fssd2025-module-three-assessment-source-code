from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config')

    @app.context_processor
    def inject_site_meta():
        return dict(
            SITE_NAME=app.config["SITE_NAME"],
            SITE_NAME_ACCESSIBLE=app.config["SITE_NAME_ACCESSIBLE"],
            SITE_TAGLINE=app.config["SITE_TAGLINE"],
        )

    return app
