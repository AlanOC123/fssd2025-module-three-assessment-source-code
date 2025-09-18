SCORING = {
    "base": 100,
    "difficulty": {
        "easy": 0.8,
        "medium": 1.0,
        "hard": 1.6,
        "enthusiast": 2.0
    },
    "streak": {
        "mode": "compound",
        "step": 1.05,
        "cap": 3.0
    },
    "speed": {
        "ceil": 2,
        "step": 0.1,
        "floor": 0.8,
        "interval": 5,
    },
    "multiple_choice_options": {
        "all_correct_bonus": 100,
        "partial_credit": True,
        "incorrect_penalty": 1
    },
    "rounding": 1
}

def get_all_correct_bonus() -> int:
    return SCORING["multiple_choice_options"]["all_correct_bonus"]

def get_speed_mul(time_s):
    ceil = SCORING["speed"]["ceil"]
    floor = SCORING["speed"]["floor"]
    step = SCORING["speed"]["step"]
    interval = SCORING["speed"]["interval"]

    return max(ceil - step * (time_s / interval), floor)

def get_difficulty_mul(key):
    return SCORING["difficulty"].get(key, 1.0)

def get_base():
    return SCORING["base"]

def get_streak_mul(streak):
    step = SCORING["streak"]["step"]
    cap = SCORING["streak"]["cap"]

    return min(step ** streak, cap)

def get_credit(truePositives, falsePositives, correct):
    pen = SCORING["multiple_choice_options"]["incorrect_penalty"]
    return max((truePositives - pen * falsePositives) / max(len(correct), 1), 0)

def get_raw(base, difficulty, streak_mult, speed_mult):
    return base * difficulty * streak_mult * speed_mult

def get_points(raw, credit):
    rounding = SCORING["rounding"]
    return round(raw * credit, rounding)

def get_final(points, bonus):
    rounding = SCORING["rounding"]
    return round(points + bonus, rounding)

def calc_score(correct, selected, streak, difficulty, time_s):
    tp = len(correct & selected)
    fp = len(selected - correct)
    all_correct = (tp == len(correct) and fp == 0)

    credit = get_credit(tp, fp, correct)

    base = get_base()
    streak_mult = get_streak_mul(streak)
    speed_mult  = get_speed_mul(time_s)
    difficulty_mult = get_difficulty_mul(difficulty)

    raw = get_raw(base, difficulty_mult, streak_mult, speed_mult)
    points = get_points(raw, credit)

    bonusCfg = SCORING["multiple_choice_options"]["all_correct_bonus"]

    bonus = bonusCfg if (len(correct) > 1 and all_correct) else 0
    awarded = get_final(points, bonus)

    return awarded, all_correct

def calc_total_score(curr_total, awarded):
    rounding = SCORING["rounding"]
    return round(curr_total + awarded, rounding)