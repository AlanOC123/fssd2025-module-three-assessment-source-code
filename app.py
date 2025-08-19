from app import create_app
from app.routes import routes_list
from app.routes.register_routes import register_routes_to_app
from app.data.interface import get_planets, get_planet_by_name, get_planet_by_id

if __name__ == '__main__':
    app = create_app()
    print(routes_list)
    register_routes_to_app(app, routes_list)
    app.run(debug=True, port=8080)
