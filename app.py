from app import create_app
from app.routes import routes_list
from app.routes.register_routes import register_routes_to_app

app = create_app()
register_routes_to_app(app, routes_list)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
