import pandas as pd
import requests
from requests_html import HTMLSession

session = HTMLSession()

r = session.get("https://www.coingecko.com/en")

df = pd.read_html(r.text)[0]

df = df[["Coin","Price","Mkt Cap"]]
df["Coin"] = df["Coin"].apply(lambda x: x.split("  ")[0])
df["Price"] = df["Price"].apply(lambda x: x.replace(",", "").replace("$",""))
df["Mkt Cap"] = df["Mkt Cap"].apply(lambda x: x.replace(",", "").replace("$",""))

print(df)
