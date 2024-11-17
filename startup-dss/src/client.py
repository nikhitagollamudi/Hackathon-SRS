import gradio as gr
from decision_support import process_inputs
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

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
        result["trend_chart"],      # File path for trend chart
        result["trend_analysis"]
    )

# Function to toggle visibility of visualizations
def toggle_visualizations(current_visibility):
    # Toggle the boolean value
    new_visibility = not current_visibility
    return (
        gr.update(visible=new_visibility),
        gr.update(visible=new_visibility),
        new_visibility
    )

# Dropdown options
industries = ["SaaS", "FinTech", "Gaming and Entertainment", "Food and Beverage", "Renewable Energy"]
kpis = [
    "Customer Acquisition Cost (CAC)", "Churn Rate", "Average Order Size",
    "Monthly Recurring Revenue (MRR)", "Annual Run Rate (ARR)", "Cash Runway",
    "Burn Rate", "K-factor", "Gross Sales", "Monthly Active Users (MAU)",
    "Net Promoter Score (NPS)", "CAC/LTV Ratio"
]

# Gradio Interface
with gr.Blocks() as demo:
    # Title
    with gr.Row():
        gr.Markdown("<h1 style='text-align: center; color: #4CAF50;'>Venture Companion</h1>")

    # Input Section
    with gr.Row():
        industry_input = gr.Dropdown(label="Select Industry", choices=industries)
        kpi_input = gr.Dropdown(label="Select KPI", choices=kpis)

    # Analyze Button
    with gr.Row():
        submit_btn = gr.Button("Analyze")

    # Recommendations Output
    with gr.Row():
        text_result = gr.Textbox(label="Recommendations", lines=12, interactive=False)
    # Trend Prediction
    with gr.Row():
        trend_result = gr.Textbox(label="Trend Prediction", lines=2, interactive=False)

    
    # Visualization Toggle Button
    with gr.Row():
        toggle_btn = gr.Button("Show/Hide Visualizations")
        # Initialize a state to keep track of visibility
        vis_state = gr.State(False)

    # Visualizations
    with gr.Row(visible=False) as vis_row:
        sentiment_chart = gr.Image(label="Sentiment Analysis Chart")
        trend_chart = gr.Image(label="Trend Analysis Chart")
    
    
    # Connect frontend inputs to backend function
    submit_btn.click(
        fn=get_kpi_analysis,
        inputs=[industry_input, kpi_input],
        outputs=[text_result, sentiment_chart, trend_chart, trend_result]
    )

    # Connect toggle button to toggle function
    toggle_btn.click(
        fn=toggle_visualizations,
        inputs=[vis_state],
        outputs=[vis_row, vis_row, vis_state]
    )

demo.launch()
