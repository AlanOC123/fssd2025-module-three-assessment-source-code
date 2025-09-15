from flask import session, request, abort, redirect, url_for
from . import bp
from app.data.interface import get_question
from .session_manager import (
    get_curr_question_id, 
    get_streak, 
    set_streak, 
    set_total_score, 
    record_attempt,
    get_total_score,
    get_state,
    get_question_ids,
    get_curr_ind,
    set_is_last_q,
    get_is_last_q,
    advance
)
from .scoring import calc_score, calc_total_score

def get_answer_data(q_data, selected_opts):
    correct_options = q_data["correctOptionIds"]
    num_correct_options = len(correct_options)

    result = []
    num_correct_attempts = 0
    num_incorrect_attempts = 0

    for opt in selected_opts:
        if opt in correct_options:
            result.append({ "chose": opt, "is_correct": True })
            num_correct_attempts += 1
        else:
            result.append({ "chose": opt, "is_correct": False })
            num_incorrect_attempts += 1

    num_attempts = num_correct_attempts + num_incorrect_attempts
    missing_attempts = num_correct_options - num_attempts
    success_percent = (num_correct_attempts / num_correct_options) * 100

    return {
        "attemptsMade": num_attempts,
        "numCorrectAttempts": num_correct_attempts,
        "missingAttempts": missing_attempts,
        "successPercent": success_percent,
        "detailedResult": result,
    }

def get_question_data(ids_list, curr_ind):
    q_id = ids_list[curr_ind]
    q_data = get_question(q_id)
    q_text = q_data["question"]
    q_options = q_data["options"]
    q_type = q_data["type"]

    return {
        "questionText": q_text,
        "questionOptions": q_options,
        "questionType": q_type
    }

def get_next_index(curr_ind, max_count):
    next_ind = curr_ind + 1
    is_finished = False

    if next_ind == max_count:
        is_finished = True

    return ( next_ind, is_finished )

def is_correct(q_opts, u_opts):
    intersect = q_opts.intersection(u_opts)

@bp.get("/next", endpoint="next")
def get_next_question():
    progress = request.args.get("progress", default="true").lower() in {"1", "true", "yes", "y"}

    delta = request.args.get("delta", default=1, type=int)

    if progress:
        advance(delta)
    
    question_ids = get_question_ids();
    curr_ind = get_curr_ind();
    curr_q_id = question_ids[curr_ind]
    max_count = len(question_ids)
    curr_q = get_question(curr_q_id)

    question_text = curr_q["question"]
    question_options = curr_q["options"]
    question_type = curr_q["type"]

    is_last_q = curr_ind == max_count - 1
    set_is_last_q(is_last_q)

    return {
        "maxCount": max_count,
        "currInd": curr_ind,
        "qText": question_text,
        "qOptions": question_options,
        "qType": question_type,
        "isLast": is_last_q
    }, 200

@bp.post("/submit", endpoint="submit")
def submit_answer():
    data = request.get_json(force=True)
    selected = set(data.get("answers", []))
    time_s = float(data.get("time", 0))

    qid = get_curr_question_id()
    q = get_question(qid)

    correct = set(q["correctOptionIds"])
    difficulty = q["difficulty"]
    curr_streak = get_streak()

    awarded, all_correct = calc_score(correct, selected, curr_streak, difficulty, time_s)

    new_score = calc_total_score(get_total_score(), awarded)

    new_streak = curr_streak + 1 if all_correct else 0

    new_attempt = {
        "qid": qid,
        "selected": list(selected),
        "correct": list(correct),
        "all_correct": all_correct,
        "points": awarded,
        "time_s": time_s,
    }

    record_attempt(new_attempt)
    set_streak(new_streak)
    set_total_score(new_score)

    is_last_q = get_is_last_q()

    if is_last_q:
        return { "redirect": url_for('quiz.result') }, 200

    # response for the popup UI
    return {
        "allCorrect": all_correct,
        "correctOpts": list(correct),
        "currentStreak": new_streak,
        "awardedPoints": awarded,
        "runningTotal": new_score,
        "timeTaken": time_s
    }, 200
