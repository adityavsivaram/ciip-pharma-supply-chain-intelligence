# India Pharma Supply Chain Intelligence System
## CIIP Index — Upstream Risk Scoring and Demand Forecasting

**Developed by Aditya V Sivaram Poduri**
**India Supply Chain Signals** | indiasupplychainsignals.substack.com

---

## Business Problem

Indian pharmaceutical manufacturers face upstream input cost volatility 
driven by cross-industry demand competition and geopolitical supply 
disruptions. Standard procurement systems monitor direct supplier 
performance but cannot detect upstream contagion signals forming 
6 to 8 weeks before they reach procurement costs.

---

## Solution Architecture

**Layer 1 — Demand Forecasting Engine**
Prophet time series models trained on 132 months of price data 
(2015 to 2025) for 5 critical pharma upstream inputs.

**Layer 2 — CIIP Index Risk Scoring**
Cross-Industry Input Pressure Index applying Input-Output economics 
to score each material on pharma demand pressure, cross-industry 
competition, and geopolitical supply risk.

**Layer 3 — Executive Decision Dashboard**
Interactive Streamlit dashboard combining forecast output and CIIP 
risk scores into a single procurement intelligence view.

---

## Key Findings (June 2026)

| Material | CIIP Score | Risk Level | 12M Forecast |
|---|---|---|---|
| LNG Japan | 9.50 | CRITICAL | UP 35.2% |
| Soda Ash | 8.67 | CRITICAL | DOWN 5.7% |
| Methanol | 7.50 | HIGH | UP 7.9% |
| Acetic Acid | 7.50 | HIGH | STABLE 1.1% |
| Polysilicon | 6.00 | MEDIUM | DOWN 59.6% |

**Critical insight:** LNG Japan at 9.5 CRITICAL with 35% price 
increase forecast represents the highest upstream risk for Indian 
pharma procurement. Energy cost escalation transmits into API 
manufacturing costs within 6 to 8 weeks.

---

## CIIP Index Scoring Methodology

CIIP Score = (Pharma Demand x 0.30) + (Cross-Industry Competition x 0.45) + (Geopolitical Risk x 0.25)

---

## Technical Stack

Python | Prophet | Pandas | NumPy | Plotly | Streamlit | scikit-learn | Matplotlib

---

## Data Sources

| Material | Source | Rating |
|---|---|---|
| Methanol | Methanex Contract Prices | PRIMARY |
| LNG Japan | World Bank Pink Sheet | PRIMARY |
| Soda Ash | FRED Reconstructed Proxy | PROXY |
| Acetic Acid | Chemanalyst/ICIS Proxy | PROXY |
| Polysilicon | PVInsights/Bloomberg Proxy | PROXY |

---

## Contact

Aditya V Sivaram Poduri
adityavsivaram@gmail.com
https://linkedin.com/in/adityasivaram

**Live Dashboard:** https://ciip-pharma-supply-chain-intelligence-eowphashbnq2jnvj6mkjzq.streamlit.app
