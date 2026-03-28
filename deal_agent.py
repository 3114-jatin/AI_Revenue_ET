def detect_deal_risk(engagement_score):

    if engagement_score < 30:
        return "High Risk: Engagement dropped"

    if engagement_score < 60:
        return "Medium Risk"

    return "Healthy Deal"