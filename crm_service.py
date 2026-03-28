from sqlalchemy.orm import Session
from models.crm_models import Lead
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_lead(name, company, email, engagement_score, deal_stage):

    db = SessionLocal()

    new_lead = Lead(
        name=name,
        company=company,
        email=email,
        engagement_score=engagement_score,
        deal_stage=deal_stage
    )

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    db.close()

    return new_lead


def get_all_leads():

    db = SessionLocal()

    leads = db.query(Lead).all()

    db.close()

    return leads


def update_engagement(lead_id, new_score):

    db = SessionLocal()

    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if lead:
        lead.engagement_score = new_score
        db.commit()

    db.close()

    return lead