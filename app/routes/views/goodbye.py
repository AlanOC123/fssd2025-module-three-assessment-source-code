from flask import Response

# test view function
def goodbye() -> Response | str:
    return 'Goodbye'
