from turtle import color
import pandas as pd
from matplotlib import pyplot as plt

# Mount cases data
cases_url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv"
col_list = ["date", "cases_new"]
cases_df = pd.read_csv(cases_url, usecols=col_list)
cases_today = cases_df

# Death Data
death_url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_malaysia.csv"
col_list = ["date", "deaths_new"]
death_df = pd.read_csv(death_url, usecols=col_list)
death_today = death_df.tail(n=1)


# Plot
x1 = cases_today.date
y1 = cases_today.cases_new

# Plot configurations
plt.figure(figsize=(10,3)) 
plt.plot(x1, y1, linestyle = 'dashed')

# Save plot with transparent background
plt.axis('off')
plt.title("New Cases", color='silver')
plt.savefig('my_plot.png', transparent=True, bbox_inches='tight')