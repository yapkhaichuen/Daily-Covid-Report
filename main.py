import pandas as pd
import datetime
import json
import pytz

# New Case Data
cases_url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv"
col_list = ["date", "cases_new"]
cases_df = pd.read_csv(cases_url, usecols=col_list)
cases_today = cases_df.tail(n=1)
case_results = int(cases_today.cases_new)

# Death Data
death_url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_malaysia.csv"
col_list = ["date", "deaths_new"]
death_df = pd.read_csv(death_url, usecols=col_list)
death_today = death_df.tail(n=1)
death_results = int(death_today.deaths_new)

# Mount date
date_dirty = str(death_today.date)[-36:]
date_current = date_dirty[:-26]

# Current time of process for server to log. Malaysian time for refrence
KL = pytz.timezone('Asia/Kuala_Lumpur')
current_time = str(datetime.datetime.now(KL))

# Summary function
def short_summary():
      summary = [
            {
            "Country": "Malaysia",
            "Last updated": date_current,
            "Cases": case_results,
            "Deaths": death_results,
            "Generated": current_time
      }
      ]
      """save data to json file"""
      with open('data.json', 'w') as outfile:
            json.dump(summary, outfile, indent=4, sort_keys=False)
      return summary

# Call function
short_summary()



