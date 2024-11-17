import pandas as pd
from sentiment_analysis import load_data, filter_news_by_kpi, analyze_sentiment
from recommendation_system import generate_dynamic_recommendations
from trend_analysis import prepare_data, train_trend_model, predict_kpi_trend
import matplotlib.pyplot as plt
import tempfile


def create_pie_chart(positive, negative, neutral):
    """
    Generate a pie chart for sentiment analysis results and save to a temporary file.
    """
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive, negative, neutral]
    colors = ['#6aa84f', '#cc0000', '#f1c232']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.axis('equal')

    # Save to a temporary file and return the file path
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(temp_file.name, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory
    return temp_file.name


def create_line_chart(dates, values, prediction=None):
    """
    Generate a line chart for KPI trend analysis and save to a temporary file.
    """
    dates = [date.strftime('%Y-%m-%d') if isinstance(date, pd.Timestamp) else date for date in dates]

    fig, ax = plt.subplots()
    ax.plot(dates, values, marker='o', label="Historical Data")
    if prediction:
        ax.plot(dates + ['Prediction'], values + [prediction], linestyle='--', marker='x', label="Prediction")
    ax.legend()
    plt.title("KPI Trend Analysis")
    plt.xlabel("Date")
    plt.ylabel("KPI Value")
    plt.xticks(rotation=45)
    plt.grid()

    # Save to a temporary file and return the file path
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(temp_file.name, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory
    return temp_file.name


def process_inputs(industry, kpi, api_key):
    """
    Process the given industry and KPI inputs and return recommendations, predictions, and visualizations.
    """
    # Load dataset
    df = load_data()

    output = {}

    try:
        # Step 1: Sentiment Analysis
        news_headlines = filter_news_by_kpi(industry, kpi, df)
        if not news_headlines:
            return {"error": f"No news headlines found for {industry} and {kpi}."}
        sentiments = analyze_sentiment(news_headlines)
        positive = sentiments.count("POSITIVE")
        negative = sentiments.count("NEGATIVE")
        neutral = len(sentiments) - positive - negative
        output["sentiment_chart"] = create_pie_chart(positive, negative, neutral)

        # Step 2: Recommendations
        recommendations = generate_dynamic_recommendations(industry, kpi, df, api_key)
        if len(recommendations) > 10:
            recommendations = recommendations[:10]
        output["recommendations"] = recommendations

        # Step 3: Trend Analysis
        X, y, sorted_data = prepare_data(df, kpi, industry)
        model = train_trend_model(X, y)
        future_predictions, trend = predict_kpi_trend(model, X, y, steps=1)
        output["trend_chart"] = create_line_chart(
            sorted_data['Date'].tolist(),
            y.tolist(),
            future_predictions[-1] if future_predictions else None
        )
        output["trend_analysis"] = f"{kpi} is expected to {'improve' if trend > 0 else 'decline'} by {abs(trend):.2f}% in the next period."

    except Exception as e:
        return {"error": str(e)}

    return output
