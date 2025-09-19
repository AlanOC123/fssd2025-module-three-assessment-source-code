from flask import render_template, session
from datetime import datetime, timezone
from . import bp
from .session_manager import (
    get_question_ids,
    get_state,
    get_attempts,
    get_total_score,
    get_longest_streak,
)
from .scoring import get_all_correct_bonus, get_base

def get_grade(count, attempts):
    all_correct_bonus = get_all_correct_bonus()
    base_score = get_base()

    all_correct = all([a.get("all_correct") for a in attempts])

    weighted_score = sum([
        a.get("score") - all_correct_bonus if (a.get("is_multi") and a.get("all_correct")) == True else a.get("points") for a in attempts
    ])

    if all_correct and attempts:
        weighted_score += 50 * count

    grade_weights = {
        "Cadet": {
            "score": base_score * 0.6 * count,
            "text": "Cadet",
            "img": 'quiz/assets/badge_cadet.webp'
        },
        "Technician": {
            "score": base_score * 0.8 * count,
            "text": "Technician",
            "img": 'quiz/assets/badge_technician.webp'
        },
        "Navigator": {
            "score": base_score * 1.0 * count,
            "text": "Navigator",
            "img": 'quiz/assets/badge_navigator.webp'
        },
        "Mission Controller": {
            "score": base_score * 1.2 * count,
            "text": "Mission Controller",
            "img": 'quiz/assets/badge_mission_controller.webp'
        },
        "Captain": {
            "score": base_score * 1.4 * count,
            "text": "Captain",
            "img": 'quiz/assets/badge_captain.webp'
        },
    }

    if weighted_score <= 0:
        return { 
            "grade": "Retry",
            "img": "quiz/assets/badge_retry.webp"
        }

    for k in grade_weights.keys():
        if  weighted_score <= grade_weights[k]["score"]:
            return {
                "text": grade_weights[k]["text"],
                "img": grade_weights[k]["img"],
            }
        
    return { 
        "grade": "Pioneer",
        "img": "quiz/assets/badge_pioneer.webp"
    }

@bp.get("/result", endpoint="result")
def result():
    attempts = get_attempts()
    qids = get_question_ids()
    score = get_total_score()
    longest_streak = get_longest_streak()
    quickest_ans = 0 if not attempts or len(attempts) is 0 else min([a.get("time_s") for a in attempts])
    count = len(qids)

    grade = get_grade(count=count, attempts=attempts)

    config = {
        "grade": grade,
        "score": score,
        "longest_streak": longest_streak,
        "quickest_ans": quickest_ans,
        "attempts": attempts
    }

    return render_template('quiz/views/result.html', config=config)