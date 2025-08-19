from flask import Response, render_template

# test view function
def index() -> Response | str:
    print(1)
    return render_template('index.html')
