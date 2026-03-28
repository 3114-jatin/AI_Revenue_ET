import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

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
# Prospect Agent
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
                st.error("Please fill in Name, Email, and Company before sending.")
            else:
                data = {
                    "name": name,
                    "email": email,
                    "company": company
                }

                response = requests.post(f"{API_URL}/outreach", json=data)

                if response.status_code == 200:
                    st.success("✅ Email Sent Successfully")
                    st.json(response.json())
                else:
                    st.error("❌ Error sending email")
                    st.write(response.text)


# -------------------------------
# Deal Risk
# -------------------------------

if menu == "Deal Risk Detection":

    st.header("⚠️ AI Deal Risk Agent")

    with st.form("deal_risk_form"):
        engagement_score = st.number_input("Engagement Score (0-100)", min_value=0, max_value=100)
        submitted = st.form_submit_button("Analyze Risk")

        if submitted:
            data = {
                "engagement_score": engagement_score
            }

            response = requests.post(f"{API_URL}/deal-risk", json=data)
            st.write(response.json())


# -------------------------------
# Churn Prediction
# -------------------------------

if menu == "Churn Prediction":

    st.header("📉 AI Churn Detection")

    with st.form("churn_form"):
        usage = st.number_input("Usage Score", min_value=0.0)
        sentiment = st.number_input("Sentiment Score", min_value=0.0)
        submitted = st.form_submit_button("Predict Churn")

        if submitted:
            data = {
                "usage": usage,
                "sentiment": sentiment
            }

            response = requests.post(f"{API_URL}/churn", json=data)

            if response.status_code == 200:
                st.success("Prediction Ready")
                st.json(response.json())
            else:
                st.error("Error")
                st.write(response.text)


# -------------------------------
# Competitive Intelligence
# -------------------------------

if menu == "Competitive Intelligence":

    st.header("🏆 AI Competitive Battlecards")

    with st.form("battlecard_form"):
        competitor = st.text_input("Competitor Name")
        submitted = st.form_submit_button("Generate Battlecard")

        if submitted:
            data = {"competitor": competitor}

            response = requests.post(f"{API_URL}/battlecard", json=data)

            if response.status_code == 200:
                st.success("Battlecard Generated")
                st.json(response.json())
            else:
                st.error("Error")
                st.write(response.text)