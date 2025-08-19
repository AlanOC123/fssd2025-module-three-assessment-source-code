from .blueprints.test import bp
from .views.index import index
from .views.goodbye import goodbye

routes_list = [
    { "rule": None, "func": None, "endpoint": None, "methods": None, "blueprint": bp },
    { "rule": '/', "func": index, "endpoint": "index", "methods": ["GET"], "blueprint": None },
    { "rule": '/goodbye', "func": goodbye, "endpoint": "goodbye", "methods": ["GET"], "blueprint": None },
]
