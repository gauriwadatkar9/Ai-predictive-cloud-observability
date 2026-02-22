# dashboard/components.py
import streamlit as st

def display_metric(name, value, threshold=80):
    if value > threshold:
        st.metric(label=name, value=value, delta="⚠️ High", delta_color="inverse")
    else:
        st.metric(label=name, value=value, delta="Normal", delta_color="normal")