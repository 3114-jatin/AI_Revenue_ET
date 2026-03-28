from services.llm_service import generate_response

def generate_battlecard(competitor):

    prompt = f"""
    Create a competitive battlecard against {competitor}.

    Include:
    - strengths
    - weaknesses
    - sales talking points
    """

    return generate_response(prompt)