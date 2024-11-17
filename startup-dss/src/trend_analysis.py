import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def prepare_data(df, kpi, industry):
    """
    Prepare historical data for the given KPI and industry.
    """
    industry_data = df[df['Industry'] == industry]

    if kpi not in industry_data.columns or industry_data[kpi].isna().all():
        raise ValueError(f"No valid data for KPI '{kpi}' in the '{industry}' industry.")

    industry_data['Date'] = pd.to_datetime(industry_data['Date'])
    sorted_data = industry_data.sort_values('Date')

    X = np.arange(len(sorted_data)).reshape(-1, 1)
    y = sorted_data[kpi].values

    return X, y, sorted_data

def train_trend_model(X, y):
    """
    Train a linear regression model to predict KPI trends.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_kpi_trend(model, X, y, steps=1):
    """
    Predict the KPI trend for the next 'steps' time periods.
    """
    future_X = np.arange(len(X), len(X) + steps).reshape(-1, 1)
    future_predictions = model.predict(future_X)

    trend = (future_predictions[-1] - y[-1]) / y[-1] * 100 if y[-1] != 0 else 0

    return future_predictions, trend
