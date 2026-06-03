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

    forecast_data = {
        "Soda Ash": {
            "dates": ["2025-01","2025-02","2025-03","2025-04","2025-05","2025-06",
                      "2025-07","2025-08","2025-09","2025-10","2025-11","2025-12"],
            "values": [358.2, 354.1, 350.8, 348.2, 346.0, 344.5,
                       343.2, 342.8, 342.5, 342.3, 342.2, 342.3],
            "upper":  [378.2, 376.1, 374.8, 374.2, 373.0, 372.5,
                       372.2, 371.8, 371.5, 371.3, 371.2, 371.3],
            "lower":  [338.2, 332.1, 326.8, 322.2, 319.0, 316.5,
                       314.2, 313.8, 313.5, 313.3, 313.2, 313.3],
        },
        "Methanol": {
            "dates": ["2025-01","2025-02","2025-03","2025-04","2025-05","2025-06",
                      "2025-07","2025-08","2025-09","2025-10","2025-11","2025-12"],
            "values": [815.0, 822.0, 830.0, 838.0, 845.0, 850.0,
                       854.0, 857.0, 860.0, 862.0, 864.0, 865.1],
            "upper":  [870.0, 882.0, 895.0, 908.0, 918.0, 925.0,
                       930.0, 934.0, 938.0, 941.0, 943.0, 945.1],
            "lower":  [760.0, 762.0, 765.0, 768.0, 772.0, 775.0,
                       778.0, 780.0, 782.0, 783.0, 785.0, 785.1],
        },
        "Acetic Acid": {
            "dates": ["2025-01","2025-02","2025-03","2025-04","2025-05","2025-06",
                      "2025-07","2025-08","2025-09","2025-10","2025-11","2025-12"],
            "values": [681.0, 682.0, 683.5, 684.0, 685.0, 685.5,
                       686.0, 686.5, 687.0, 687.2, 687.3, 687.4],
            "upper":  [720.0, 724.0, 728.0, 730.0, 732.0, 733.0,
                       734.0, 735.0, 736.0, 736.5, 737.0, 737.5],
            "lower":  [642.0, 640.0, 639.0, 638.0, 638.0, 638.0,
                       638.0, 638.0, 638.0, 638.0, 637.5, 637.3],
        },
        "LNG Japan": {
            "dates": ["2025-01","2025-02","2025-03","2025-04","2025-05","2025-06",
                      "2025-07","2025-08","2025-09","2025-10","2025-11","2025-12"],
            "values": [12.8, 13.2, 13.6, 14.0, 14.3, 14.7,
                       15.0, 15.3, 15.6, 15.8, 16.0, 16.2],
            "upper":  [14.5, 15.2, 15.8, 16.5, 17.0, 17.8,
                       18.5, 19.0, 19.5, 20.0, 20.5, 21.0],
            "lower":  [11.1, 11.2, 11.4, 11.5, 11.6, 11.7,
                       11.5, 11.6, 11.7, 11.5, 11.5, 11.4],
        },
        "Polysilicon": {
            "dates": ["2025-01","2025-02","2025-03","2025-04","2025-05","2025-06",
                      "2025-07","2025-08","2025-09","2025-10","2025-11","2025-12"],
            "values": [8.2, 7.8, 7.4, 7.0, 6.6, 6.2,
                       5.8, 5.4, 5.0, 4.6, 4.2, 3.6],
            "upper":  [10.5, 10.2, 9.8, 9.4, 9.0, 8.6,
                       8.2, 7.8, 7.4, 7.0, 6.5, 6.0],
            "lower":  [5.9, 5.4, 5.0, 4.6, 4.2, 3.8,
                       3.4, 3.0, 2.7, 2.4, 2.1, 1.8],
        },
    }

    selected = st.selectbox("Select material to view forecast:", list(forecast_data.keys()))
    row = df[df["Material"] == selected].iloc[0]
    unit = row["Unit"]
    fd = forecast_data[selected]

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=fd["dates"], y=fd["upper"],
        mode="lines", line=dict(width=0),
        showlegend=False, name="Upper"
    ))
    fig2.add_trace(go.Scatter(
        x=fd["dates"], y=fd["lower"],
        mode="lines", fill="tonexty",
        fillcolor="rgba(212,117,10,0.15)",
        line=dict(width=0),
        name="Confidence Band"
    ))
    fig2.add_trace(go.Scatter(
        x=fd["dates"], y=fd["values"],
        mode="lines+markers",
        name="12M Forecast",
        line=dict(color="#D4750A", width=2.5),
        marker=dict(size=6)
    ))
    fig2.update_layout(
        paper_bgcolor="#0d1117",
        plot_bgcolor="#0d1117",
        font=dict(color="white"),
        xaxis=dict(gridcolor="#21262d", title="Month"),
        yaxis=dict(gridcolor="#21262d", title=f"Price ({unit})"),
        height=420,
        title=dict(
            text=f"{selected} — CIIP: {row['CIIP_Score']} ({row['Risk_Level']}) | "
                 f"12M Direction: {row['Forecast']}",
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
    st.caption("Forecasts generated using Facebook Prophet on 132 months of historical data (2015-2025). "
               "Pre-computed outputs shown for dashboard stability.")

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

CIIP Score = (Pharma Demand x 0.30) + (Cross-Industry Competition x 0.45) + (Geopolitical Risk x 0.25)

**Analytical Weights Applied:**
- Volatility weight (CV and extreme moves)
- Import dependency weight (India sourcing exposure)
- Energy correlation weight (LNG transmission linkage)
- Supplier concentration weight (single-country risk)

---

**Forecasting Method:**
- Model: Facebook Prophet (Meta, 2017)
- Training: 132 monthly observations (2015-2025)
- Horizon: 12 months forward
- Validation: Walk-forward train/test split — MAPE, MAE, RMSE

---

**Limitations:**
1. Three datasets are reconstructed proxies: Soda Ash (FRED), Acetic Acid (Chemanalyst), Polysilicon (PVInsights)
2. CIIP input scores are expert-calibrated, not regression-derived
3. Prophet accuracy degrades beyond 6-month horizon for volatile materials
4. Polysilicon has structural break in 2022 — treat as LOW CONFIDENCE
5. Model does not capture black swan events

**Data Credibility:** PRIMARY = authoritative source | PROXY = reconstructed estimate

---
    """)
