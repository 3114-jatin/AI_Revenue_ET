import streamlit as st
import pandas as pd

from prospect_agent import generate_outreach
from deal_agent import detect_deal_risk
from churn_agent import predict_churn
from competitive_agent import generate_battlecard

st.set_page_config(page_title="AI Revenue Intelligence", layout="wide")

st.title("🚀 AI Revenue Intelligence Dashboard")

menu = st.sidebar.selectbox(
    "Choose Agent",
    [
        "Prospect Outreach",
        "Deal Risk Detection",
        "Churn Prediction",
        "Competitive Intelligence"
    ]
)

# -------------------------------
# Prospect Outreach
# -------------------------------

if menu == "Prospect Outreach":

    st.header("📧 AI Prospecting Agent")

    with st.form("outreach_form"):
        name = st.text_input("Prospect Name")
        email = st.text_input("Prospect Email")
        company = st.text_input("Company")

        submitted = st.form_submit_button("Generate Outreach Email")

        if submitted:

            if not name.strip() or not email.strip() or not company.strip():
                st.error("Please fill all fields")

            else:
                try:
                    result = generate_outreach(name, email, company)

                    st.success("✅ Email Generated Successfully")
                    st.write(result)

                except Exception as e:
                    st.error("❌ Error generating email")
                    st.write(e)

# -------------------------------
# Deal Risk Detection
# -------------------------------

if menu == "Deal Risk Detection":

    st.header("⚠️ AI Deal Risk Detection")

    with st.form("deal_form"):

        engagement_score = st.slider(
            "Engagement Score",
            0,
            100,
            50
        )

        submitted = st.form_submit_button("Analyze Deal")

        if submitted:

            try:
                result = detect_deal_risk(engagement_score)

                st.success("Analysis Complete")
                st.write(result)

            except Exception as e:
                st.error("Error analyzing deal")
                st.write(e)

# -------------------------------
# Churn Prediction
# -------------------------------

if menu == "Churn Prediction":

    st.header("📉 AI Customer Churn Prediction")

    with st.form("churn_form"):

        usage = st.number_input(
            "Usage Score",
            min_value=0.0,
            step=1.0
        )

        sentiment = st.number_input(
            "Customer Sentiment Score",
            min_value=0.0,
            step=1.0
        )

        submitted = st.form_submit_button("Predict Churn")

        if submitted:

            try:
                result = predict_churn(usage, sentiment)

                st.success("Prediction Generated")
                st.write(result)

            except Exception as e:
                st.error("Prediction Error")
                st.write(e)

# -------------------------------
# Competitive Intelligence
# -------------------------------

if menu == "Competitive Intelligence":

    st.header("🏆 AI Competitive Battlecards")

    with st.form("battlecard_form"):

        competitor = st.text_input("Competitor Name")

        submitted = st.form_submit_button("Generate Battlecard")

        if submitted:

            if not competitor.strip():
                st.error("Please enter competitor name")

            else:
                try:
                    result = generate_battlecard(competitor)

                    st.success("Battlecard Generated")
                    st.write(result)

                except Exception as e:
                    st.error("Error generating battlecard")
                    st.write(e)
