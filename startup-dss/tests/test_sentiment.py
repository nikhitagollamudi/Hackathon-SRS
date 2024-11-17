from sentiment_analysis import load_data, filter_news_by_kpi, analyze_sentiment

def test_analyze_sentiment():
    df = load_data()
    headlines = filter_news_by_kpi("SaaS", "Churn Rate", df)
    sentiments = analyze_sentiment(headlines)
    assert len(sentiments) == len(headlines)
