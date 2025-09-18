from flask import request, session, redirect, url_for
from . import bp
from app.data.interface import get_questions, get_subjects
from random import choice
from .session_manager import init_quiz, get_quiz_in_progress, clear_session

def filter_questions(difficulty: str, subjects_arr: list) -> list:
    return list(
        filter(
            lambda q: 
            (q.get("difficulty") == difficulty) 
            and any(tag in subjects_arr for tag in q.get("tags", [])), 
            get_questions()
        )
    )

def pick_questions(filtered_questions: list, count: int) -> list:
    question_bank = []
    available_questions = filtered_questions;

    for _ in range(count):
        if len(available_questions) == 0:
            print("Not enough questions, expand scope")
            break
            
        curr_question = choice(available_questions)
        ind = available_questions.index(curr_question)

        if curr_question:
            question_bank.append(curr_question)

        available_questions.pop(ind)

    return question_bank

def build_questions(options) -> list: 
    filters = options.get("filters")
    count = options.get("count")
    difficulty = filters.get('difficulty')
    subjects = filters.get("subjects")
    num_subjects = filters.get("subjects_count")

    if num_subjects == 0:
        subjects = get_subjects()

    selected_questions = pick_questions(
        filter_questions(difficulty=difficulty, subjects_arr=subjects), 
        count=count
    )

    return [q["id"] for q in selected_questions]

@bp.post('/build', endpoint="build")
def build():
    clear_session()

    count = int(request.form.get("question-count"))
    difficulty = request.form.get("question-difficulty")
    time_limit = request.form.get("time-limit")
    subjects = request.form.getlist("subjects")

    options = { 
        "count": count,
        "filters": {
            "difficulty": difficulty,
            "subjects": subjects,
            "subjects_count": len(subjects)
        } 
    }

    questions = build_questions(options)
    
    init_quiz(questions, time_limit)

    return redirect(url_for('quiz.play'))