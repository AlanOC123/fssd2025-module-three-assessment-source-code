from flask import Flask, Blueprint
from typing import Iterable, Mapping

# define structure of view functions iterable
ViewSpec = Mapping[str, object]

# validate a blueprint
def validate_blueprint(blueprint, blueprint_set: set) -> tuple:

    # if blueprint is none, skip (happy path)
    if not blueprint:
        return (None, None)

    # if return an error if one exists
    if not isinstance(blueprint, Blueprint):
        return (blueprint, TypeError(f"Invalid blueprint type: {type(blueprint)}"))

    if blueprint.name in blueprint_set:
        return (blueprint, ValueError(f"Duplicate blueprint {blueprint.name}"))

    # return the blueprint without the error (happy path)
    return (blueprint, None)

def validate_rule(rule) -> tuple:

    # check for a type or value error
    if not isinstance(rule, str):
        return (rule, TypeError(f"Invalid rule type: {type(rule)}"))

    if not rule.startswith('/'):
        return (rule, ValueError(f"Rule must start with '/'. Rule: {rule!r}"))

    return (rule, None)

def validate_endpoint(endpoint, endpoint_list:set) -> tuple:

    # check for a type or value error
    if not isinstance(endpoint, str):
        return (endpoint, ValueError(f"Invalid endpoint: {endpoint!r}"))

    if endpoint in endpoint_list:
        return (endpoint, ValueError(f"Duplicate endpoint: {endpoint}"))

    return (endpoint, None)

def validate_func(func) -> tuple:

    # check the function is callable
    if not callable(func):
        return (func, TypeError(f"View function must be a callable function: {func!r}"))

    return (func, None)

def validate_methods_list(methods_list) -> tuple:

    # convert missing methods to a default
    if not methods_list:
        return (["GET"], None)

    # check types
    if isinstance(methods_list, str):
        methods_list = [methods_list]
    elif not isinstance(methods_list, (list, tuple)):
        return (methods_list, TypeError(f"methods must be str | list[str], got: {type(methods_list)}"))

    for method in methods_list:
        if not isinstance(method, str):
            return (methods_list, TypeError(f"invalid HTTP method type, got: {type(method)}"))

    # allowed HTTP methods set
    allowed = { "GET", "POST", "PUT", "PATCH", "DELETE" }

    # convert to upper
    normalised = [method.upper() for method in methods_list]

    # check if they are acceptable
    for method in normalised:
        if method not in allowed:
            return (methods_list, ValueError(f"invalid HTTP method name, got: {method}"))

    return (normalised, None)

def register_routes_to_app(app: Flask, routes: Iterable[ViewSpec]) -> None:

    if not routes:
        raise ValueError("no routes given to register.")

    # declare sets for duplicate tracking
    seen_endpoints = set()
    seen_blueprints = set()

    # iterate over viewspecs
    for spec in routes:
        # check blueprint first
        bp, bpError = validate_blueprint(spec.get("blueprint"), seen_blueprints)

        # register blueprint and continue iteration
        if bp:
            if bpError:
                raise bpError
            else:
                app.register_blueprint(bp)
                seen_blueprints.add(bp.name)
                continue

        # get values and errors
        rule, ruleError = validate_rule(spec.get("rule"))
        func, funcError = validate_func(spec.get("func"))
        endpoint, endpointError = validate_endpoint(spec.get("endpoint"), seen_endpoints)
        methods, methodsError = validate_methods_list(spec.get("methods"))

        # iterate over errors and raise if any exist
        for error in [ruleError, funcError, endpointError, methodsError]:
            if error:
                raise error

        # add the view function to the app
        app.add_url_rule(rule=rule, view_func=func, endpoint=endpoint, methods=methods)
        seen_endpoints.add(endpoint)
