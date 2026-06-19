# The CIIP Index (Cross-Industry Input Pressure Index)

**Developed by Aditya V. Sivaram Poduri**

## Analytical Framework & Methodology

The CIIP Index is a proprietary framework applying Leontief Input-Output economics to track cross-industry commodity demand contagion in India's pharma supply chain — covering soda ash, methanol, acetic acid, LNG Japan, and polysilicon.

This repository hosts the **India Pharma Supply Chain Intelligence System**, the working implementation of the CIIP Index: upstream risk scoring combined with demand forecasting for India's pharmaceutical manufacturing sector.

**India Supply Chain Signals** | indiasupplychainsignals.substack.com

---

## Further Reading

- [The Soda Ash Signal: Why India's Pharma Supply Chain Has a Blind Spot No Control Tower Can See](https://medium.com/@adityavsivaram/the-soda-ash-signal-why-indias-pharma-supply-chain-has-a-blind-spot-no-control-tower-can-see-0a46b1a45999) — Medium

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
|---
