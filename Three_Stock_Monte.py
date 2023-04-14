#!/usr/bin/env python
# coding: utf-8

# ##  Monte Carlo Simulation
# 
# We retrieve stock price data using the Alpaca API and simulate multiple portfolio compositions using Monte Carlo Simulation.

# ### Import Dependencies

# In[60]:


# Import libraries and dependencies
import os
import pandas as pd
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation


# In[61]:


# Load .env enviroment variables
from dotenv import load_dotenv
load_dotenv()


# In[62]:


# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version = "v2"
)


# ### Get Past ~4 Year's Worth of Stock Price Data via Alpaca API Call

# In[63]:


# Set timeframe to "1Day"
timeframe = "1Day"

# Set start and end datetimes between now and 4 years ago.
start_date = pd.Timestamp("2020-05-01", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2023-04-01", tz="America/New_York").isoformat()

# Set the ticker information
tickers = ["FVRR","QFIN", "ROKU"]

# Get 4 year's worth of historical price data
# HINT: Set "limit" to at least 10000 so all ticker rows are captured from get_bars()
df_ticker = api.get_bars(
    tickers,
    timeframe,
    start=start_date,
    end=end_date
).df

# Display sample data
df_ticker.head()


# > Note: We're going to simulate five years of growth below, and so we might want to pull at least five years of data in order to do that. But we pulled four because of Alpaca's rate limits--we can only pull 1,000 rows per ticker at a time (approximately four years of data, with 252 tradable days per year). If we pull data with repeated calls in a `for` loop, however, we can get quite a few more years than what we've got above.  

# In[64]:


# Reorganize the DataFrame
# Separate ticker data
FVRR = df_ticker[df_ticker["symbol"]=="FVRR"].drop("symbol", axis=1)
ROKU = df_ticker[df_ticker["symbol"]=="ROKU"].drop("symbol", axis=1)
SAVA = df_ticker[df_ticker["symbol"]=="SAVA"].drop("symbol", axis=1)
#TWLO = df_ticker[df_ticker["symbol"]=="TWLO"].drop("symbol", axis=1)
#QFIN = df_ticker[df_ticker["symbol"]=="QFIN"].drop("symbol", axis=1)


# Concatenate the ticker DataFrames
df_ticker = pd.concat([FVRR, ROKU, SAVA], axis=1, keys=["FVRR","ROKU","SAVA"])

# Display sample data
df_ticker.head()


# ### Simulate five year portfolio growth with evenly-distributed stock investments

# In[65]:


# Configure a Monte Carlo simulation to forecast five years cumulative returns
MC_even_dist = MCSimulation(
    portfolio_data = df_ticker,
    weights = [.33,.33,.33],
    num_simulation = 1000,
    num_trading_days = 252*5
)

# Print the simulation input data
MC_even_dist.portfolio_data.head()


# In[66]:


# Run a Monte Carlo simulation to forecast five years cumulative returns
MC_even_dist.calc_cumulative_return()


# In[67]:


# Plot simulation outcomes
line_plot = MC_even_dist.plot_simulation()


# In[68]:


# Plot probability distribution and confidence intervals
dist_plot = MC_even_dist.plot_distribution()


# In[69]:


# Fetch summary statistics from the Monte Carlo simulation results
even_tbl = MC_even_dist.summarize_cumulative_return()

# Print summary statistics
print(even_tbl)


# In[ ]:


# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $15,000 investments in stocks
even_ci_lower = round(even_tbl[8]*15000,2)
even_ci_upper = round(even_tbl[9]*15000,2)

# Print results
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${even_ci_lower} and ${even_ci_upper}.")


# ### Simulate five year portfolio growth with 60% SAVA
# stock

# In[ ]:


# Configure a Monte Carlo simulation to forecast five years cumulative returns with 60% SAVA stock
MC_SAVA = MCSimulation(
    portfolio_data = df_ticker,
    weights = [.20,.60,.20],
    num_simulation = 1000,
    num_trading_days = 252*5)

# Print the simulation input data
MC_SAVA.portfolio_data.head()


# In[ ]:


# Run a Monte Carlo simulation to forecast five years cumulative returns with 60% SAVA stock
MC_SAVA.calc_cumulative_return()


# In[ ]:


# Plot simulation outcomes
SAVA_line_plot = MC_SAVA.plot_simulation()


# In[ ]:


# Plot probability distribution and confidence intervals
SAVA_dist_plot = MC_SAVA.plot_distribution()


# In[ ]:


# Fetch summary statistics from the Monte Carlo simulation results
SAVA_tbl = MC_SAVA.summarize_cumulative_return()

# Print summary statistics
print(SAVA_tbl)


# In[ ]:


# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $15,000 investments
SAVA_ci_lower = round(att_tbl[8]*15000,2)
SAVA_ci_upper = round(att_tbl[9]*15000,2)

# Print results
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${SAVA_ci_lower} and ${SAVA_ci_upper}.")


# ### Simulate five year portfolio growth with 60% Nike stock

# In[ ]:


# Configure a Monte Carlo simulation to forecast five years cumulative returns with 60% ROKU stock
MC_ROKU = MCSimulation(
    portfolio_data = df_ticker,
    weights = [.60,.20,.20],
    num_simulation = 1000,
    num_trading_days = 252*5
)

# Printing the simulation input data
MC_ROKU.portfolio_data.head()


# In[ ]:


# Run a Monte Carlo simulation to forecast five years cumulative returns with 60% Nike stock
MC_ROKU.calc_cumulative_return()


# In[ ]:


# Plot simulation outcomes
ROKU_line_plot = MC_ROKU.plot_simulation()


# In[ ]:


# Plot probability distribution and confidence intervals
ROKU_dist_plot = MC_ROKU.plot_distribution()


# In[ ]:


# Fetch summary statistics from the Monte Carlo simulation results
ROKU_tbl = MC_ROKU.summarize_cumulative_return()

# Print summary statistics
print(ROKU_tbl)


# In[ ]:


# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $15,000 investments
ROKU_ci_lower = round(nike_tbl[8]*15000,2)
ROKU_ci_upper = round(nike_tbl[9]*15000,2)

# Print results
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${ROKU_ci_lower} and ${ROKU_ci_upper}.")


# ### Simulate five year portfolio growth with 60% FVRR stock

# In[ ]:


# Configuring a Monte Carlo simulation to forecast five years cumulative returns
MC_FVRR = MCSimulation(
    portfolio_data = df_ticker,
    weights = [.20,.20,.60],
    num_simulation = 1000,
    num_trading_days = 252*5)

# Printing the simulation input data
MC_FVRR.portfolio_data


# In[ ]:


# Run a Monte Carlo simulation to forecast five years cumulative returns with 60% FVRR stock
MC_FVRR.calc_cumulative_return()


# In[ ]:


# Plot simulation outcomes
FVRR_line_plot = MC_FVRR.plot_simulation()


# In[ ]:


# Plot probability distribution and confidence intervals
FVRR_dist_plot = MC_FVRR.plot_distribution()


# In[ ]:


# Fetch summary statistics from the Monte Carlo simulation results
FVRR_tbl = MC_FVRR.summarize_cumulative_return()

# Print summary statistics
print(FVRR_tbl)


# In[ ]:


# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $15,000 investments
FVRR_ci_lower = round(FVRR_tbl[8]*15000,2)
FVRR_ci_upper = round(FVRR_tbl[9]*15000,2)

# Print results
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${FVRR_ci_lower} and ${FVRR_ci_upper}.")


# ### Summarize findings across all 4 simulations

# In[ ]:


# Even weighted stocks
print("Even weighted stocks")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${even_ci_lower} and ${even_ci_upper}.")
print("*"*50)

# 60% for SAVA
print("60% for SAVA")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${SAVA_ci_lower} and ${SAVA_ci_upper}.")
print("*"*50)

# 60% for FVRR
print("60% for FVRR")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${FVRR_ci_lower} and ${FVRR_ci_upper}.")
print("*"*50)

# 60% for ROKU
print("60% for ROKU")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${ROKU_ci_lower} and ${ROKU_ci_upper}.")
print("*"*50)


# Looking across all four simulations, the portfolio breakdown with the greatest chance of success looks to be the portfolio with a majority of Nike stock. Although all four portfolios have a chance to lose money, the Nike portfolio is roughly the same level of risk with far more upside potential.
