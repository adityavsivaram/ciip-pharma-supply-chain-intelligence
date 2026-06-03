import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="India Pharma Supply Chain Intelligence System",
    layout="wide"
)

st.title("India Pharma Supply Chain Intelligence System")
st.caption("CIIP Index v2.0 | Aditya V Sivaram Poduri | India Supply Chain Signals")
st.divider()

ciip_data = {
    "Material":      ["Soda Ash", "Methanol", "Acetic Acid", "LNG Japan", "Polysilicon"],
    "CIIP_Score":    [8.67, 7.50, 7.50, 9.50, 6.00],
    "Weighted_CIIP": [8.80, 7.90, 8.10, 9.80, 5.70],
    "Risk_Level":    ["CRITICAL", "HIGH", "HIGH", "CRITICAL", "MEDIUM"],
    "Confidence":    ["MODERATE", "HIGH", "MODERATE", "HIGH", "LOW"],
    "Conf_Score":    [68.0, 81.0, 64.0, 79.0, 51.0],
    "Forecast":      ["DOWN 5.7%", "UP 7.9%", "STABLE 1.1%", "UP 35.2%", "DOWN 59.6%"],
    "Last_Price":    [362.90, 802.00, 680.00, 12.00, 9.00],
    "Unit":          ["USD/MT", "USD/MT", "USD/MT", "USD/MMBtu", "USD/KG"],
    "Action": [
        "IMMEDIATE: Review safety stock. Activate alternate sourcing.",
        "URGENT: Monitor weekly. Prepare contingency plan.",
        "URGENT: Monitor weekly. Prepare contingency plan.",
        "IMMEDIATE: Review working capital exposure.",
        "WATCH: Monthly review. Document exposure."
    ]
}
df = pd.DataFrame(ciip_data)

col1, col2, col3, col4 = st.columns(4)
col1.metric("CRITICAL Materials", int((df["Risk_Level"] == "CRITICAL").sum()), "Immediate action required")
col2.metric("HIGH Risk Materials", int((df["Risk_Level"] == "HIGH").sum()), "Weekly monitoring required")
col3.metric("Avg CIIP Score", f"{df['CIIP_Score'].mean():.2f}", "Portfolio risk level")
col4.metric("Avg Weighted Score", f"{df['Weighted_CIIP'].mean():.2f}", "Analytically adjusted")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "Risk Scorecard", "Forecasts", "Scenario Analysis", "Methodology"
])

with tab1:
    st.subheader("CIIP Risk Scorecard")
    color_map = {
        "CRITICAL": "#c00000",
        "HIGH":     "#D4750A",
        "MEDIUM":   "#d4a017",
        "LOW":      "#059669"
    }
    fig = go.Figure(go.Bar(
        y=df["Material"],
        x=df["Weighted_CIIP"],
        orientation="h",
        marker_color=[color_map[r] for r in df["Risk_Level"]],
        text=[f"{s} — {r} | Conf: {c}%" for s, r, c in zip(
            df["Weighted_CIIP"], df["Risk_Level"], df["Conf_Score"])],
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Weighted CIIP: %{x}<br>%{customdata}<extra></extra>",
        customdata=df["Action"]
    ))
    fig.add_vline(x=8.0, line_dash="dash", line_color="#c00000",
                  opacity=0.5, annotation_text="CRITICAL threshold")
    fig.add_vline(x=6.5, line_dash="dash", line_color="#D4750A",
                  opacity=0.5, annotation_text="HIGH threshold")
    fig.update_layout(
        paper_bgcolor="#0d1117",
        plot_bgcolor="#0d1117",
        font=dict(color="white"),
        xaxis=dict(range=[0, 13], gridcolor="#21262d", title="Weighted CIIP Score (0–10)"),
        yaxis=dict(gridcolor="#21262d"),
        height=380,
        margin=dict(r=220, l=20, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(
        df[["Material", "CIIP_Score", "Weighted_CIIP", "Risk_Level",
            "Confidence", "Forecast", "Action"]],
        hide_index=True,
        use_container_width=True
    )

with tab2:
    st.subheader("Upstream Price Forecasts — 12-Month Forward")
    files_map = {
        "Soda Ash":    "Soda_Ash_2015_2025.csv",
        "Methanol":    "Methanol_2015_2025.csv",
        "Acetic Acid": "Acetic_Acid_2015_2025.csv",
        "LNG Japan":   "LNG_Japan_2015_2025.csv",
        "Polysilicon": "Polysilicon_2015_2025.csv"
    }
    selected = st.selectbox("Select material to view forecast:", list(files_map.keys()))

    @st.cache_data
    def get_forecast(material_name, fname):
        d = pd.read_csv(fname).rename(columns={"Date": "ds", "Price": "y"})
        d["ds"] = pd.to_datetime(d["ds"])
        d = d.sort_values("ds").reset_index(drop=True)
        m = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=False,
            daily_seasonality=False,
            changepoint_prior_scale=0.05
        )
        m.fit(d)
        future = m.make_future_dataframe(periods=12, freq="MS")
        forecast = m.predict(future)
        return d, forecast

    with st.spinner(f"Running Prophet model for {selected}..."):
        act, fore = get_forecast(selected, files_map[selected])

    row = df[df["Material"] == selected].iloc[0]
    unit = row["Unit"]
    fore_only = fore[fore["ds"] > act["ds"].max()]

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=act["ds"], y=act["y"],
        mode="markers", name="Actual",
        marker=dict(color="white", size=4, opacity=0.7)
    ))
    fig2.add_trace(go.Scatter(
        x=fore["ds"], y=fore["yhat"],
        mode="lines", name="Model Fit / Forecast",
        line=dict(color="#D4750A", width=2)
    ))
    fig2.add_trace(go.Scatter(
        x=pd.concat([fore_only["ds"], fore_only["ds"][::-1]]),
        y=pd.concat([fore_only["yhat_upper"], fore_only["yhat_lower"][::-1]]),
        fill="toself",
        fillcolor="rgba(212,117,10,0.15)",
        line=dict(color="rgba(0,0,0,0)"),
        name="Confidence Band"
    ))
    fig2.add_vline(
        x=act["ds"].max().timestamp() * 1000,
        line_dash="dash", line_color="gray",
        opacity=0.5, annotation_text="Forecast Start"
    )
    fig2.update_layout(
        paper_bgcolor="#0d1117",
        plot_bgcolor="#0d1117",
        font=dict(color="white"),
        xaxis=dict(gridcolor="#21262d", title="Date"),
        yaxis=dict(gridcolor="#21262d", title=f"Price ({unit})"),
        height=420,
        title=dict(
            text=f"{selected} — CIIP: {row['CIIP_Score']} ({row['Risk_Level']}) | 12M: {row['Forecast']}",
            font=dict(color="white", size=13)
        ),
        legend=dict(bgcolor="#161b22", bordercolor="#21262d")
    )
    st.plotly_chart(fig2, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Last Price", f"{row['Last_Price']} {unit}")
    c2.metric("12M Forecast Direction", row["Forecast"])
    c3.metric("Confidence", f"{row['Confidence']} ({row['Conf_Score']}%)")
    st.info(f"Procurement Action: {row['Action']}")

with tab3:
    st.subheader("Scenario Intelligence — Enterprise Stress Testing")
    scenario = st.selectbox("Select scenario:", [
        "S1 — LNG Surge +40% (Hormuz Escalation)",
        "S2 — China Export Controls",
        "S3 — India Solar PLI Acceleration"
    ])
    shock_map = {
        "S1 — LNG Surge +40% (Hormuz Escalation)":
            {"LNG Japan": 0.40, "Methanol": 0.15, "Acetic Acid": 0.10},
        "S2 — China Export Controls":
            {"Acetic Acid": 0.25, "Methanol": 0.20, "Polysilicon": -0.30},
        "S3 — India Solar PLI Acceleration":
            {"Soda Ash": 0.20, "Polysilicon": 0.15, "LNG Japan": 0.08}
    }
    shocks = shock_map[scenario]
    results = []
    risk_order = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}
    for _, row in df.iterrows():
        shock = shocks.get(row["Material"], 0)
        geo_amp = 1.30 if abs(shock) > 0.20 else 1.15 if abs(shock) > 0.10 else 1.0
        base_geo = {"Soda Ash": 2, "Methanol": 3,
                    "Acetic Acid": 3, "LNG Japan": 3, "Polysilicon": 3}
        cross = ({"Soda Ash": 3, "Methanol": 1, "Acetic Acid": 1,
                  "LNG Japan": 3, "Polysilicon": 3}[row["Material"]] +
                 {"Soda Ash": 3, "Methanol": 2, "Acetic Acid": 1,
                  "LNG Japan": 3, "Polysilicon": 1}[row["Material"]] +
                 {"Soda Ash": 2, "Methanol": 1, "Acetic Acid": 2,
                  "LNG Japan": 2, "Polysilicon": 1}[row["Material"]]) / 3
        pharma = {"Soda Ash": 3, "Methanol": 3,
                  "Acetic Acid": 3, "LNG Japan": 3, "Polysilicon": 1}
        new_geo = min(3, base_geo[row["Material"]] * geo_amp)
        raw = (pharma[row["Material"]] * 0.30 + cross * 0.45 + new_geo * 0.25)
        new_ciip = round(raw * (10 / 3), 2)
        old_risk = row["Risk_Level"]
        new_risk = ("CRITICAL" if new_ciip >= 8.0 else
                    "HIGH" if new_ciip >= 6.5 else
                    "MEDIUM" if new_ciip >= 5.0 else "LOW")
        escalated = risk_order.get(new_risk, 0) > risk_order.get(old_risk, 0)
        results.append({
            "Material":      row["Material"],
            "Shock Applied": f"{shock * 100:+.0f}%",
            "Base CIIP":     row["CIIP_Score"],
            "Scenario CIIP": new_ciip,
            "Delta":         round(new_ciip - row["CIIP_Score"], 2),
            "Base Risk":     old_risk,
            "Scenario Risk": new_risk,
            "Escalates":     "YES" if escalated else "—"
        })
    sc_df = pd.DataFrame(results)
    st.dataframe(sc_df, hide_index=True, use_container_width=True)
    escalations = sc_df[sc_df["Escalates"] == "YES"]
    if len(escalations) > 0:
        st.error(f"{len(escalations)} material(s) escalate to a higher risk tier in this scenario: "
                 + ", ".join(escalations["Material"].tolist()))
    else:
        st.success("No risk tier escalations in this scenario.")

with tab4:
    st.subheader("Methodology and Limitations")
    st.markdown("""
**Framework:** CIIP Index — Cross-Industry Input Pressure Index  
**Theoretical Basis:** Leontief Input-Output Economics (Nobel Prize 1973)  
**Version:** 2.0 — June 2026  
**Developer:** Aditya V Sivaram Poduri

---

**Scoring Formula:**
