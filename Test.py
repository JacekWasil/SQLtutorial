import sqlite3
import requests
from bs4 import BeautifulSoup

# Request URL
response = requests.get("https://books.toscrape.com/catalogue/category/books/history_32/index.html")
aaa = BeautifulSoup(response.text, "html.parser")
books = aaa.find_all("button")
print(books[0])
