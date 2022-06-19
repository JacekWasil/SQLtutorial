import pandas as pd
import requests
from requests_html import HTMLSession

session = HTMLSession()

r = session.get("https://www.bankier.pl/waluty/kursy-walut/nbp")

df = pd.read_html(r.text)[0]


print(df)
