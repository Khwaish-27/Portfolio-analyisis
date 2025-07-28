

---

### 📄 **README.md – Mutual Fund Beta Calculation Project**

```markdown
# 📊 Mutual Fund Beta, Standard Deviation & Jensen's Alpha Calculator

This project calculates key risk metrics — **Beta**, **Standard Deviation**, and **Jensen's Alpha** — for a list of mutual fund schemes compared to a benchmark index.

---

## 📁 Project Structure

```

Internship Beta Project.xlsx
├── Sheet 1: Fund List (with Scheme Codes)
├── Sheet 2..n-1: AMC-wise NAV data (includes 'Scheme Code', 'Date', 'Price')
└── Sheet n: Benchmark Index data (includes 'Date', 'Price')

```

---

## ✅ What the Script Does

1. Reads the mutual fund list from the first sheet.
2. Identifies benchmark index data from the **last sheet**.
3. Loops through all AMC NAV sheets to match scheme codes.
4. For each matched fund:
   - Cleans and aligns NAV & benchmark data.
   - Calculates:
     - **Daily Returns**
     - **Beta** (fund's sensitivity to the benchmark)
     - **Standard Deviation** (volatility of returns)
     - **Jensen's Alpha** (risk-adjusted performance)
5. Outputs the results into a structured Excel file.

---

## 📊 Output

The script exports the analysis results to:

```

portfolio\_analysis\_results.xlsx

````

This file contains:
- Scheme Code
- AMC Sheet (data source)
- Beta
- Standard Deviation
- Jensen’s Alpha

---

## ⚙️ Requirements

Make sure the following Python packages are installed:

```bash
pip install pandas numpy openpyxl
````

---

## 🧮 Key Formulae Used

* **Daily Return** = (Today’s NAV - Yesterday’s NAV) / Yesterday’s NAV
* **Beta** = Cov(Fund Return, Benchmark Return) / Var(Benchmark Return)
* **Jensen's Alpha** = (Fund Return - Rf) - Beta × (Benchmark Return - Rf)

> Risk-Free Rate (Rf) assumed = 6.5% annually, converted to daily: `0.065 / 252`

---

## 📌 Notes

* Scheme codes are normalized to string format to ensure consistency.
* Returns are computed using `pct_change()` on NAV and benchmark price.
* Insufficient data for any fund results in a warning but does not stop execution.
* Benchmark should have daily data matching the NAV dates.

---

## 👤 Author

**Khwaish Mankotia**
Internship Beta Project – 2025

```

---


```
# Portfolio-analyisis
