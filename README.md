# Hackathon Startup Decision Support System (SRS)

## Overview
The **Venture Companion** is a data-driven platform designed to empower entrepreneurs by providing **actionable recommendations** based on **industry-specific KPIs**. This project was developed as part of a hackathon challenge to assist startups in aligning their business strategies with market trends and insights.

---

## Features

1. **Sentiment Analysis**:
   - Analyzes industry news headlines using NLP techniques.
   - Classifies headlines into **positive**, **negative**, or **neutral** sentiment.

2. **Trend Analysis**:
   - Uses historical data and machine learning models like linear regression to identify KPI trends over time.
   - Provides insights into past performance and future projections.

3. **AI-Driven Recommendations**:
   - Combines sentiment and trend analysis to generate **top 10 strategic recommendations** tailored to specific industries and KPIs.

4. **Interactive Dashboard**:
   - Users can interact with the platform via a responsive web interface, receiving visualized insights and data-driven guidance.

---

## Dataset
- **File**: `startup_kpi_data.csv`
- **Contents**:
  - Industry-specific metrics (e.g., SaaS, FinTech, Gaming).
  - KPIs: Customer Acquisition Cost (CAC), Monthly Recurring Revenue (MRR), Churn Rate, Net Promoter Score (NPS), etc.
  - News headlines summarizing trends and developments from 2011 to 2024.

## Tech Stack
- **Programming Language**: Python
- **Libraries**:
  - **Data Analysis**: Pandas, NumPy
  - **Visualization**: Matplotlib
  - **Machine Learning**: Scikit-learn
  - **Natural Language Processing**: Hugging Face Transformers (for sentiment analysis)
  - **Backend Framework**: Flask (optional for deployment)
- **Other Tools**:
  - `.env` for environment variables
  - `Gradio` for a user-friendly interface (optional)


