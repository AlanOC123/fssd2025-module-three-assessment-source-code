from flask import session

_TIME_LIMIT_MAP = {
    "short": 300,
    "medium": 600,
    "long": 900,
    "unlimited": None,
}

def init_quiz(question_ids=[], time_limit_key="unlimited"):
    time_limit_s = _TIME_LIMIT_MAP[time_limit_key]

    session["quiz"] = {
        "is_init": True,
        "question_ids": question_ids,
        "curr_ind": 0,
        "total_score": 0.0,
        "streak": 0,
        "attempts": [],
        "time_limit_s": time_limit_s,
        "time_limit_key": time_limit_key,
        "time_left_s": 0,
        "in_progress": False,
        "is_finished": False,
        "is_last_q": False,
        "longest_streak": 0
    }

def get_question_ids() -> list:
    return session.get("quiz").get("question_ids", [])

def get_quiz_in_progress() -> bool:
    return session.get("quiz").get("in_progress", False)

def get_quiz_is_finished() -> bool:
    return session.get("quiz").get("is_finished", False)

def get_curr_ind() -> int:
    return session.get("quiz").get("curr_ind", 0)

def get_curr_question_id() -> dict | None:
    quiz = session.get("quiz")
    return quiz["question_ids"][get_curr_ind()]

def get_total_score() -> float:
    return session.get("quiz").get("total_score", 0.0)

def get_streak() -> int:
    return session.get("quiz").get("streak", 0)

def get_is_last_q() -> bool:
    return session.get("quiz").get("is_last_q", False)

def get_longest_streak() -> int:
    return session.get("quiz").get("longest_streak", 0)

def get_time_limit() -> int:
    return session.get("quiz").get("time_limit_s", 0)

def get_time_left() -> int:
    return session.get("quiz").get("time_left_s", 0)

def advance(delta=1) -> None:
    curr = session.get("quiz")
    total = len(get_question_ids())
    curr["curr_ind"]  = max(0, min(curr["curr_ind"] + delta, total - 1))
    session["quiz"] = curr

def set_total_score(new_score: float) -> None:
    curr = session.get("quiz")
    curr["total_score"] = new_score
    session["quiz"] = curr

def set_streak(new_streak: int) -> None:
    curr = session.get("quiz")
    curr["streak"] = new_streak
    session["quiz"] = curr

def record_attempt(attempt: dict) -> None:
    curr = session.get("quiz")
    attempts = curr["attempts"]

    attempts.append(attempt)

    curr["attempts"] = attempts
    session["quiz"] = curr

def clear_session() -> None:
    _last_saved_config = get_state()

    session["quiz"] = {
        "is_init": False,
        "in_progress": False,
        "is_finished": False,
    }

def get_state() -> dict:
    return session.get("quiz", None)

def get_attempts() -> list:
    return session.get("quiz").get("attempts")

def set_in_progress(state: bool) -> None:
    curr = session.get("quiz")
    curr["in_progress"] = state
    session["quiz"] = curr

def set_is_last_q(state: bool) -> None:
    curr = session.get("quiz")
    curr["is_last_q"] = state
    session["quiz"] = curr

def set_is_finished(state: bool) -> None:
    curr = session.get("quiz")
    curr["is_finished"] = state
    session["quiz"] = curr

def set_longest_streak(new_streak) -> None:
    curr = session.get("quiz")
    curr_longest = curr["longest_streak"]
    curr["longest_streak"] = max(new_streak, curr_longest)
    session["quiz"] = curr

def set_time_left(timeS) -> None:
    curr = session.get("quiz")
    curr_time_s = curr["time_left_s"]
    curr["time_left_s"] = max(timeS, 0)
    session["quiz"] = curr

def restart():
    qids = session["quiz"]["question_ids"]
    time_limit_key = session["quiz"]["time_limit_key"]
    
    if not qids or not time_limit_key:
        raise ValueError("Missing config settings")
    
    init_quiz(qids, time_limit_key)

def save_state() -> None:
    curr_state = get_state()
    print(curr_state)