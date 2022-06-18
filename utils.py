import json


def load_data() -> list[dict]:
    """
    Function returns data from json file.

    :return: list[dict] of candidates
    """

    with open('candidates.json', 'r', encoding='utf-8') as f:
        candidates = json.load(f)
        return candidates


def format_candidates(candidates: list[dict]) -> str:
    """
    Function return formatted string of candidate

    :param candidates: list[dict]
    :return: str
    """

    result = '<pre>'

    for candidate in candidates:
        result += f"""
Имя кандидата: {candidate["name"]}
Позиция кандидата: {candidate["position"]}
Навыки: {candidate["skills"]}
        """
    result += '<pre>'
    return result


def get_all_candidates() -> list[dict]:
    """
    Function return all candidates from data

    :return: list[dict]
    """

    return load_data()


def get_candidate_by_id(uid: int) -> dict | None:
    """
    Function return candidate by ID

    :param uid: int
    :return: dict
    """

    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


def get_candidate_by_skill(skill: str) -> list[dict]:
    """
    Function return candidates by skill

    :param skill: str
    :return: list[dict]
    """

    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
