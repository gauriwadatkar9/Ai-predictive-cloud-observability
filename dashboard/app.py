# dashboard/app.py
import streamlit as st
import json
from processing.risk_scoring import calculate_risk
from processing.alert_clustering import cluster_alerts
from processing.ai_explainer import explain_incident
from processing.cost_correlation import calculate_cost_impact
from processing.timeline_narrator import generate_timeline
from dashboard.components import display_metric
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide", page_title="AI Cloud Observability", page_icon="🛰️")
st.title("AI-Powered Cloud Observability Platform")

# Load simulated metrics
with open("mock_data.json") as f:
    metrics = json.load(f)

alerts = ["CPU spike", "Memory high", "Service 2 slow"]

# Top metrics
col1, col2, col3 = st.columns(3)
risk = calculate_risk(metrics['CPU Usage'], metrics['Memory Usage'], metrics['Errors'])
risk_color = "green" if risk > 70 else "orange" if risk > 40 else "red"
col1.metric("System Health Score", f"{risk}/100", delta_color=risk_color)
cost = calculate_cost_impact(metrics['CPU Usage'], metrics['Memory Usage'])
col2.metric("Estimated Cost Impact ($)", f"${cost}")
clustered = cluster_alerts(alerts)
col3.write("## Alerts")
for incident in clustered:
    st.markdown(f"<div style='padding:5px;margin:5px;border-radius:5px;background-color:#FFA500;color:white;'>{incident}</div>", unsafe_allow_html=True)

# Tabs for Beginner / Advanced
tab1, tab2 = st.tabs(["Beginner View", "Advanced View"])
with tab1:
    st.subheader("Live Metrics")
    for name, value in metrics.items():
        display_metric(name, value)
    st.subheader("AI Root Cause Explanation")
    st.write(explain_incident(alerts))

with tab2:
    st.subheader("Metrics History")
    data = pd.DataFrame({
        "Time": [f"T-{i} min" for i in range(5,0,-1)],
        "CPU Usage": [metrics['CPU Usage']-i*2 for i in range(5)],
        "Memory Usage": [metrics['Memory Usage']-i*1 for i in range(5)],
        "Errors": [max(0, metrics['Errors']-i) for i in range(5)]
    })
    fig = px.line(data, x="Time", y=["CPU Usage","Memory Usage"], markers=True,
                  color_discrete_sequence=["#1f77b4","#2ca02c"])
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Incident Timeline Narration")
    st.text(generate_timeline(alerts))