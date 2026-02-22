# dashboard/app.py

import sys
import os
import json
import time
import pandas as pd
import streamlit as st
import plotly.express as px

# Add the project root folder to sys.path so 'processing' modules are found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import processing layer modules
from processing.risk_scoring import calculate_risk
from processing.alert_clustering import cluster_alerts
from processing.ai_explainer import explain_incident
from processing.cost_correlation import correlate_cost
from processing.timeline_narrator import narrate_timeline

# Import components
from components import display_metric

# -----------------------------
# Page config
st.set_page_config(
    page_title="AI Predictive Cloud Observability",
    page_icon="☁️",
    layout="wide",
)

st.title("☁️ AI-Powered Predictive Cloud Observability Platform")
st.markdown(
    "Monitor servers, Docker containers, and Kubernetes clusters with AI-based predictive intelligence."
)

# -----------------------------
# Load metrics
mock_file = os.path.join(os.path.dirname(__file__), "mock_data.json")

def load_metrics():
    try:
        with open(mock_file, "r") as f:
            data = json.load(f)
        return data
    except:
        return {"CPU Usage": 0, "Memory Usage": 0, "Errors": 0, "Response Time(ms)": 0}

# -----------------------------
# Sidebar: User mode
mode = st.sidebar.radio("Select Mode:", ["Beginner", "Advanced"])

# -----------------------------
# Metrics section
st.subheader("System Metrics")
metrics = load_metrics()
col1, col2, col3, col4 = st.columns(4)
display_metric("CPU Usage (%)", metrics["CPU Usage"], threshold=80)
display_metric("Memory Usage (%)", metrics["Memory Usage"], threshold=80)
display_metric("Errors", metrics["Errors"], threshold=5)
display_metric("Response Time (ms)", metrics["Response Time(ms)"], threshold=800)

# -----------------------------
# AI Predictive Risk Score
st.subheader("AI Predictive Risk Score")
risk_score = calculate_risk(
    metrics["CPU Usage"], metrics["Memory Usage"], metrics["Errors"]
)
st.metric(label="System Health Score (0-100)", value=risk_score)

# -----------------------------
# Alert Clustering
st.subheader("Alert Clustering")
alerts = cluster_alerts(metrics)
if alerts:
    for alert in alerts:
        st.warning(f"{alert}")
else:
    st.success("No critical alerts!")

# -----------------------------
# Cost Correlation
st.subheader("Cost-Performance Correlation")
cost_impact = correlate_cost(metrics)
st.info(f"Estimated Cost Impact: ${cost_impact:.2f}")

# -----------------------------
# Timeline Narrator
st.subheader("Incident Timeline Narrator")
timeline_text = narrate_timeline(metrics)
st.write(timeline_text)

# -----------------------------
# Beginner / Advanced Views
if mode == "Advanced":
    st.subheader("Advanced Metrics Dashboard")
    # Example interactive chart using Plotly
    df = pd.DataFrame([metrics])
    fig = px.bar(
        df,
        y=["CPU Usage", "Memory Usage", "Errors", "Response Time(ms)"],
        x=["Metrics"],
        title="Detailed System Metrics",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
st.markdown("---")
st.caption("Prototype built for hackathon submission — AI-powered predictive cloud observability platform.")