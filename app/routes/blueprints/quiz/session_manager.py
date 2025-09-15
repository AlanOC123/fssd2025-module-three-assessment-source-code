from flask import session

_TIME_LIMIT_MAP = {
    "short": 300,
    "medium": 600,
    "long": 900,
    "unlimited": None,
}

def init_quiz(question_ids, time_limit_key):
    time_limit_s = _TIME_LIMIT_MAP[time_limit_key]

    session["quiz"] = {
        "is_init": True,
        "question_ids": question_ids,
        "curr_ind": 0,
        "total_score": 0.0,
        "streak": 0,
        "attempts": [],
        "time_limit_s": time_limit_s,
        "in_progress": False,
        "is_finished": False,
        "is_last_q": False,
    }

def get_question_ids() -> list:
    return session["quiz"]["question_ids"]

def get_quiz_in_progress() -> bool:
    return session["quiz"]["in_progress"]

def get_quiz_is_finished() -> bool:
    return session["quiz"]["is_finished"]

def get_curr_ind() -> int:
    return session["quiz"].get("curr_ind", 0)

def get_curr_question_id() -> dict | None:
    quiz = session["quiz"]
    return quiz["question_ids"][get_curr_ind()]

def get_total_score() -> float:
    return session["quiz"]["total_score"]

def get_streak() -> int:
    return session["quiz"]["streak"]

def get_is_last_q() -> bool:
    return session["quiz"]["is_last_q"]

def advance(delta=1) -> None:
    curr = session["quiz"]
    total = len(get_question_ids())
    curr["curr_ind"]  = max(0, min(curr["curr_ind"] + delta, total - 1))
    session["quiz"] = curr

def set_total_score(new_score: float) -> None:
    curr = session["quiz"]
    curr["total_score"] = new_score
    session["quiz"] = curr

def set_streak(new_streak: int) -> None:
    curr = session["quiz"]
    curr["streak"] = new_streak
    session["quiz"] = curr

def record_attempt(attempt: dict) -> None:
    curr = session["quiz"]
    attempts = curr["attempts"]

    attempts.append(attempt)

    curr["attempts"] = attempts
    session["quiz"] = curr

def clear_session() -> None:
    session["quiz"] = {
        "is_init": False,
        "in_progress": False,
        "is_finished": False,
    }

def get_state() -> dict:
    return session["quiz"]

def set_in_progress(state: bool) -> None:
    curr = session["quiz"]
    curr["in_progress"] = state
    session["quiz"] = curr

def set_is_last_q(state: bool) -> None:
    curr = session["quiz"]
    curr["is_last_q"] = state
    session["quiz"] = curr