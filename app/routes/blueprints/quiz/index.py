from flask import Response, render_template, session
from . import bp

@bp.get('/', endpoint='index')
def index() -> Response | str:
    is_session_started = session.get('is_session_running')

    quiz_builder_data = [
        {
            "id": "question-count",
            "name": "question-count",
            "type": "radio",
            "legend": "Question Count",
            "values": [
                { "id": "five", "text": "Five", "value": 5, "is_default": False },
                { "id": "ten", "text": "Ten", "value": 10, "is_default": True },
                { "id": "fifteen", "text": "Fifteen", "value": 15, "is_default": False },
                { "id": "twenty", "text": "Twenty", "value": 20, "is_default": False },
                { "id": "twenty-five", "text": "Twenty-Five", "value": 25, "is_default": False },
            ]
        },
        {
            "id": "question-difficulty",
            "name": "question-difficulty",
            "type": "radio",
            "legend": "Question Difficulty",
            "values": [
                { "id": "easy", "text": "Easy", "value": "easy", "is_default": False },
                { "id": "medium-difficulty", "text": "Medium", "value": "medium","is_default": True },
                { "id": "hard", "text": "Hard", "value": "hard", "is_default": False },
                { "id": "enthusiast", "text": "Enthusiast", "value": "enthusiast", "is_default": False },
            ]
        },
        {
            "id": "time-limit",
            "name": "time-limit",
            "type": "radio",
            "legend": "Time Limit",
            "values": [
                { "id": "short", "text": "Short", "value": "short", "is_default": False },
                { "id": "medium-time-limit", "text": "Medium", "value": "medium", "is_default": True },
                { "id": "long", "text": "Long", "value": "long", "is_default": False },
                { "id": "unlimited", "text": "No Limit", "value": "unlimited", "is_default": False },
            ]
        },
        {
            "id": "subjects",
            "name": "subjects",
            "type": "checkbox",
            "legend": "Subjects",
            "values": [
                {
                    "id": "exploration",
                    "text": 'Exploration',
                    "icon_class": "fa-solid fa-earth-europe",
                    "options": [
                        { "id": "earth", "text": "Earth", "value": "earth" },
                        { "id": "mars", "text": "Mars", "value": "mars" },
                        { "id": "jupiter", "text": "Jupiter", "value": "jupiter" },
                        { "id": "venus", "text": "Venus", "value": "venus" },
                        { "id": "neptune", "text": "Neptune", "value": "neptune" },
                        { "id": "uranus", "text": "Uranus", "value": "uranus" },
                        { "id": "mercury", "text": "Mercury", "value": "mercury" },
                        { "id": "saturn", "text": "Saturn", "value": "saturn" },
                        { "id": "pluto", "text": "Pluto", "value": "pluto" },
                    ]
                },
                {
                    "id": "history",
                    "text": 'History',
                    "icon_class": "fa-solid fa-landmark-dome",
                    "options": [
                        { "id": "1950s", "text": "1950s", "value": "1950s" },
                        { "id": "1960s", "text": "1960s", "value": "1960s" },
                        { "id": "1970s", "text": "1970s", "value": "1970s" },
                        { "id": "1980s", "text": "1980s", "value": "1980s" },
                        { "id": "1990s", "text": "1990s", "value": "1990s" },
                        { "id": "2000s", "text": "2000s", "value": "2000s" },
                        { "id": "2010s", "text": "2010s", "value": "2010s" },
                        { "id": "2020s", "text": "2020s", "value": "2020s" },
                    ]
                },
            ]
        },
    ]

    return render_template(
        'quiz/views/index.html', 
        quiz_data=quiz_builder_data, 
        is_session_started=is_session_started
    )
