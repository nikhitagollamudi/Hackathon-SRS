import pandas as pd

def load_data():
    """
    Load the dataset containing industry, KPI, and news headline information.
    """
    df = pd.read_csv("data/startup_kpi_data.csv")
    print("Loaded DataFrame:")
    print(df.head())  # Debugging: Check the loaded data
    return df

def filter_news_by_kpi(industry, kpi, df):
    """
    Filter news headlines relevant to the given industry and KPI.
    """
    # Ensure column names match your CSV file
    if 'Industry' not in df.columns or 'News Headline' not in df.columns:
        raise ValueError("Dataset is missing required columns: 'Industry' or 'News Headline'.")

    if kpi not in df.columns:
        raise ValueError(f"KPI '{kpi}' not found in dataset columns.")

    # Filter by industry and valid KPI values
    filtered_df = df[(df['Industry'] == industry) & (df[kpi].notna())]
    return filtered_df['News Headline'].tolist()

def analyze_sentiment(headlines):
    """
    Analyze sentiment for a list of headlines. (Placeholder function)
    Returns a list of "POSITIVE", "NEGATIVE", or "NEUTRAL".
    """
    # Placeholder: Mock sentiment analysis
    import random
    sentiments = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    return [random.choice(sentiments) for _ in headlines]
