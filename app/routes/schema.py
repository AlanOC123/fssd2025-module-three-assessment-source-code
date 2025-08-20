def get_blueprint_schema(blueprint):
    return { "blueprint": blueprint }

def get_view_schema(rule, func, endpoint, methods) -> dict:
    return { "rule": rule, "func": func, "endpoint": endpoint, "methods": methods }
