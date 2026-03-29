import pandas as pd
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model_trained = False


def train_model():
    global model_trained

    data = pd.read_csv("crm_sample_data.csv")

    X = data[["usage", "tickets", "engagement"]]
    y = data["churn"]

    model.fit(X, y)

    model_trained = True


def predict_churn(usage, tickets, engagement):

    global model_trained

    if not model_trained:
        train_model()

    prediction = model.predict([[usage, tickets, engagement]])

    if prediction[0] == 1:
        return "⚠️ Likely to Churn"

    return "✅ Healthy Customer"
