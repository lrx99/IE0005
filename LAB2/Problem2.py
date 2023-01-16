import pandas as pd

html_data = pd.read_html('https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table', match='2016 Summer Olympics medal table')

print(len(html_data))
