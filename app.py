from flask import Flask
from utils import *


app = Flask(__name__)


@app.route('/')
def page_main():
    """Main page view"""
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Candidate by id view"""
    candidates: dict = get_candidate_by_id(uid)
    result = f'<img src ="{candidates["picture"]}">'
    result += format_candidates([candidates])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    """Candidate by skill view"""
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result


app.run()
