import gradio as gr
from decision_support import process_inputs
import os

# Fetch API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Function to get KPI analysis and visuals
def get_kpi_analysis(industry, kpi):
    result = process_inputs(industry, kpi, api_key)
    if "error" in result:
        return result["error"], None, None, None

    recommendations = result["recommendations"]
    recommendations_text = "\n".join([f"{i+1}. {rec}" for i, rec in enumerate(recommendations)])

    return (
        recommendations_text,
        result["sentiment_chart"],  # File path for sentiment chart
        result["trend_chart"],     # File path for trend chart
        result["trend_analysis"]
    )

# Dropdown options
industries = ["SaaS", "FinTech", "Gaming and Entertainment", "Food and Beverage", "Renewable Energy"]
kpis = [
    "Customer Acquisition Cost (CAC)", "Churn Rate", "Average Order Size",
    "Monthly Recurring Revenue (MRR)", "Annual Run Rate (ARR)", "Cash Runway",
    "Burn Rate", "K-factor", "Gross Sales", "Monthly Active Users (MAU)",
    "Net Promoter Score (NPS)", "CAC/LTV Ratio"
]

# CSS Theme
theme_styles = """
    body {
        font-family: Arial, sans-serif;
        background-color: #1A1A19;
        color: #F6FCDF;
        margin: 0;
        padding: 0;
    }
    .gradio-container {
        background-color: #1A1A19;
    }
    .gr-button {
        background-color: #31511E;
        color: #F6FCDF;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
    .gr-button:hover {
        background-color: #859F3D;
        color: #1A1A19;
    }
    .gr-dropdown {
        background-color: #F6FCDF;
        color: #31511E;
        border-radius: 5px;
    }
    .textbox {
        background-color: #F6FCDF;
        color: #31511E;
    }
"""

# Gradio Interface
with gr.Blocks(css=theme_styles) as demo:
    with gr.Row():
        gr.Markdown("<h1>Startup KPI Analyzer</h1>")

    with gr.Row():
        industry_input = gr.Dropdown(label="Select Industry", choices=industries)
        kpi_input = gr.Dropdown(label="Select KPI", choices=kpis)

    with gr.Row():
        submit_btn = gr.Button("Analyze")

    with gr.Row():
        text_result = gr.Textbox(label="Recommendations", lines=12, interactive=False)
    
    with gr.Row():
        sentiment_chart = gr.Image(label="Sentiment Analysis Chart")
        trend_chart = gr.Image(label="Trend Analysis Chart")
    
    with gr.Row():
        trend_result = gr.Textbox(label="Trend Prediction", lines=2, interactive=False)

    # Connect frontend inputs to backend function
    submit_btn.click(
        fn=get_kpi_analysis,
        inputs=[industry_input, kpi_input],
        outputs=[text_result, sentiment_chart, trend_chart, trend_result]
    )

demo.launch()
