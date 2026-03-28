import pandas as pd
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

def train_model():

    data = pd.read_csv("backend/data/crm_sample_data.csv")

    X = data[["usage", "tickets", "engagement"]]
    y = data["churn"]

    model.fit(X, y)

def predict_churn(usage, tickets, engagement):

    pred = model.predict([[usage, tickets, engagement]])

    return "Likely to Churn" if pred[0] == 1 else "Healthy"