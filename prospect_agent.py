from llm_service import generate_response

def generate_outreach(company, person, role):

    prompt = f"""
    Write a highly personalized sales outreach email.

    Company: {company}
    Person: {person}
    Role: {role}

    Focus on solving business pain points.
    """

    return generate_response(prompt)
