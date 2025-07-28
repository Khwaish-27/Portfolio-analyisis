import pandas as pd
import numpy as np
from datetime import datetime
from scipy.stats import linregress

def calculate_returns(nav_series):
    return nav_series.pct_change().dropna()

def calculate_beta_alpha(fund_returns, benchmark_returns, risk_free_rate=0.05):
    excess_fund = fund_returns - risk_free_rate / 252
    excess_benchmark = benchmark_returns - risk_free_rate / 252
    beta, alpha, _, _, _ = linregress(excess_benchmark, excess_fund)
    return beta, alpha * 252  # Annualize alpha

def calculate_std(fund_returns):
    return fund_returns.std() * np.sqrt(252)

def main():
    input_file = 'internship beta project.xlsx'
    output_file = 'Mutual_Fund_Analysis_Output.xlsx'

    try:
        xls = pd.ExcelFile(input_file)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # Load AUM Info
    try:
        aum_df = pd.read_excel(xls, sheet_name='Sheet1')
        aum_df['Daily AUM'] = pd.to_numeric(aum_df['Daily AUM'], errors='coerce')
        aum_df = aum_df.dropna(subset=['Daily AUM'])
        aum_df['Scheme Code'] = aum_df['Scheme Code'].astype(str)
    except Exception as e:
        print(f"Error processing Sheet1: {e}")
        return

    top_30 = aum_df.sort_values(by='Daily AUM', ascending=False).head(30)

