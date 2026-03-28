from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from agents.prospect_agent import generate_outreach
from agents.deal_agent import detect_deal_risk
from agents.churn_agent import predict_churn
from agents.competitive_agent import generate_battlecard
from services.crm_service import create_lead, get_all_leads
from email_service import send_email, ALERT_EMAIL_RECIPIENT

app = FastAPI()

def _send_alert(subject: str, body: str):
    try:
        send_email(ALERT_EMAIL_RECIPIENT, subject, body)
        return True, None
    except Exception as exc:
        return False, str(exc)


class Prospect(BaseModel):
    name: str
    email: EmailStr
    company: str

@app.get("/")
def home():
    return {"message": "AI Sales Agent Running"}


@app.post("/create-lead")
def create(name:str, company:str, email:str):

    lead = create_lead(name,company,email,50,"prospect")

    return {"lead_created": lead.id}

@app.post("/outreach")
def outreach(prospect: Prospect):

    message = f"""
Hi {prospect.name},

We help companies like {prospect.company} improve sales pipeline efficiency using AI-driven revenue operations.

Would love to connect!

Best,
AI Sales Agent
"""

    send_email(
        prospect.email,
        "AI Sales Outreach",
        message
    )

    return {"status": "email sent"}

@app.get("/leads")
def leads():

    return get_all_leads()


@app.get("/outreach")
def outreach(company: str, person: str, role: str):

    email = generate_outreach(company, person, role)

    return {"email": email}

class DealRequest(BaseModel):
    engagement_score: int


# ✅ FIXED DEAL RISK PART
@app.post("/deal-risk")
def deal_risk(data: DealRequest):

    risk = detect_deal_risk(data.engagement_score)
    subject = "Deal Risk Detection Alert"
    body = (
        f"Deal risk analysis completed.\n"
        f"Engagement score: {data.engagement_score}\n"
        f"Risk result: {risk}\n"
    )
    alert_sent, alert_error = _send_alert(subject, body)

    response = {"risk_analysis": risk, "alert_sent": alert_sent}
    if alert_error:
        response["alert_error"] = alert_error

    return response


@app.get("/churn")
def churn(usage:int, tickets:int, engagement:int):

    result = predict_churn(usage,tickets,engagement)
    subject = "Churn Prediction Alert"
    body = (
        f"Churn prediction completed.\n"
        f"Usage: {usage}\n"
        f"Tickets: {tickets}\n"
        f"Engagement: {engagement}\n"
        f"Prediction: {result}\n"
    )
    alert_sent, alert_error = _send_alert(subject, body)

    response = {"churn_prediction": result, "alert_sent": alert_sent}
    if alert_error:
        response["alert_error"] = alert_error

    return response


@app.post("/churn")
def churn():
    return {"message": "Churn prediction executed"}


@app.get("/battlecard")
def battlecard(competitor:str):

    card = generate_battlecard(competitor)
    subject = "Competitive Intelligence Alert"
    body = (
        f"Competitive intelligence request completed.\n"
        f"Competitor: {competitor}\n"
        f"Battlecard summary returned.\n"
    )
    alert_sent, alert_error = _send_alert(subject, body)

    response = {"battlecard": card, "alert_sent": alert_sent}
    if alert_error:
        response["alert_error"] = alert_error

    return response

class Competitor(BaseModel):
    competitor: str


@app.post("/battlecard")
def battlecard(data: Competitor):
    card = generate_battlecard(data.competitor)
    subject = "Competitive Intelligence Alert"
    body = (
        f"Competitive intelligence request completed.\n"
        f"Competitor: {data.competitor}\n"
        f"Battlecard summary returned.\n"
    )
    alert_sent, alert_error = _send_alert(subject, body)

    response = {"battlecard": card, "alert_sent": alert_sent}
    if alert_error:
        response["alert_error"] = alert_error

    return response