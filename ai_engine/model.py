import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    X = df[['leave_days']]
    y = df['burnout_risk']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model
