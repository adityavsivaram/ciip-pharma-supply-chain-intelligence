# CIIP Forward Test: prediction record

**Recorded on:** 16 November 2026
**Recorded by:** Aditya V Sivaram Poduri

This file replaces any earlier table of CIIP scores in this Project. If another table or chat shows different scores, this file is the correct one.

## 1\. The scores being tested

These are the base CIIP scores from the pharma repository, as committed on 19 June 2026. They were fixed before any July or August 2026 price data existed.

|Material|Base CIIP score|Tier|
|-|-|-|
|LNG Japan|9.50|CRITICAL|
|Soda ash|8.67|CRITICAL|
|Methanol|7.50|HIGH|
|Acetic acid|7.50|HIGH|
|Polysilicon|6.00|MEDIUM|

Formula: CIIP Score = (Pharma Demand x 0.30) + (Cross-Industry Competition x 0.45) + (Geopolitical Risk x 0.25), inputs rated 1 to 3, result scaled to 0-10.

## 2\. The prediction

**Between August and November 2026, the inputs with a base CIIP score of 8 or above (LNG, soda ash) will gain more in price than the inputs scored below 8 (methanol, acetic acid).**

Using the base CIIP score committed on 19 June 2026.

### How it will be judged

* Measure: percentage change in price, USD per metric tonne, from August 2026 to November 2026.
* Source: the same India trade statistics source used for the June to August table below.
* PASS: the percentage change of LNG and of soda ash are both higher than the percentage change of methanol and of acetic acid.
* FAIL: anything else.
* Polysilicon is left out, because the source has no usable price for it.

### Result (fill in when November 2026 data is published)

|Material|August 2026 (USD/MT)|November 2026 (USD/MT)|Change|
|-|-|-|-|
|LNG|780.22|||
|Soda ash|226.42|||
|Methanol|479.05|||
|Acetic acid|465.22|||

Verdict: \_\_\_\_\_\_ Date checked: \_\_\_\_\_\_

## 2b. Test 2: fully forward (added 19 November 2026)

**From November 2026 to February 2027, the average percentage price change of the two highest-scored inputs (LNG, soda ash) will be higher than the average percentage price change of the two lower-scored inputs (methanol, acetic acid).**

Using the base CIIP score committed on 19 June 2026. Test 1 above is unchanged and will also be reported.

### How it will be judged

* Measure: percentage change in price, USD per metric tonne, from November 2026 to February 2027.
* Source: the same India trade statistics source as Test 1.
* PASS: the average change of LNG and soda ash is higher than the average change of methanol and acetic acid.
* FAIL: anything else.
* Every input's own change is reported, not only the averages.
* Polysilicon is left out, because the source has no usable price for it.

### Result (fill in when February 2027 data is published)

|Material|November 2026 (USD/MT)|February 2027 (USD/MT)|Change|
|-|-|-|-|
|LNG||||
|Soda ash||||
|Methanol||||
|Acetic acid||||

Average of LNG and soda ash: \_\_\_\_\_\_ Average of methanol and acetic acid: \_\_\_\_\_\_
Verdict: \_\_\_\_\_\_ Date checked: \_\_\_\_\_\_

## 3\. What was observed before this prediction

This table is an observation, not a passed test, because the prediction sentence was written after the data was seen.

|Material|Base CIIP score|June 2026 (USD/MT)|August 2026 (USD/MT)|Change|
|-|-|-|-|-|
|LNG|9.50|680.07|780.22|+14.7%|
|Soda ash|8.67|201.63|226.42|+12.3%|
|Acetic acid|7.50|505.28|465.22|-7.9%|
|Methanol|7.50|600.70|479.05|-20.3%|
|Polysilicon|6.00|no usable data|no usable data||

Source: India trade statistics, pulled on 16 November 2026. Exact source name and link: https://tradestat.commerce.gov.in/meidb/commoditywise\_import

Notes on the data: LNG is the India aggregate, not Japan-specific. Soda ash is subject to an aggregation caveat. Data was available up to August 2026 only.

## 4\. Rules for this test

1. The five base scores above are not changed until the test is judged.
2. The scoring code and the notebook in the repository are not edited until the test is judged, so the 19 June 2026 commit date stays as evidence.
3. The "analytically weighted" score is not used. It exists in two different versions (notebook and live dashboard).
4. The scores 6.90, 7.20 and 5.10 are not used. They do not appear on the dashboard or in the notebook chart.
5. A CIIP score is a ranking of pressure between inputs. It is not a forecast of price direction.

