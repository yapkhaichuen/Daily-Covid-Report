# Daily-covid-report
[![Generate Report](https://github.com/yapkhaichuen/daily-covid-report/actions/workflows/generate-report.yml/badge.svg)](https://github.com/yapkhaichuen/daily-covid-report/actions/workflows/generate-report.yml)

Generates a simple report about the current Covid-19 cases and deaths in Malaysia.
Results are delay one day, data provided by 
the Ministry of Health Malaysia covid-19 public data.

1. data.json file for report output
2. timezone-test.py to find out all timezone

Data from: <br>
https://github.com/MoH-Malaysia/covid19-public

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=https://raw.githubusercontent.com/yapkhaichuen/daily-covid-report/main/data.json) -->
<!-- The below code snippet is automatically added from https://raw.githubusercontent.com/yapkhaichuen/daily-covid-report/main/data.json -->
```json
[
    {
        "cases": 3229,
        "country": "Malaysia",
        "date-last-updated": "2022-01-19",
        "death": 13,
        "generated": "2022-01-20 12:27:20.778503+08:00"
    }
]
```
<!-- MARKDOWN-AUTO-DOCS:END -->

<!-- MARKDOWN-AUTO-DOCS:START (JSON_TO_HTML_TABLE:src=./data.json) -->
<table class="JSON-TO-HTML-TABLE"><thead><tr><th class="cases-th">cases</th><th class="country-th">country</th><th class="date-last-updated-th">date-last-updated</th><th class="death-th">death</th><th class="generated-th">generated</th></tr></thead><tbody ><tr ><td class="cases-td td_num">3229</td><td class="country-td td_text">Malaysia</td><td class="date-last-updated-td td_text">2022-01-19</td><td class="death-td td_num">13</td><td class="generated-td td_text">2022-01-20 12:27:20.778503+08:00</td></tr></tbody></table>
<!-- MARKDOWN-AUTO-DOCS:END -->


