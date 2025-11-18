# 📰 News Headlines Web Scraper

This project is a simple Python-based web scraper that extracts top news headlines from a public news website (BBC) using requests and BeautifulSoup.
The script parses <h2> tags from the webpage and saves the extracted headlines into a text file.

# 🎯 Objective

Automate data collection by scraping real-time news headlines from a live website.

# 🛠 Technologies Used

Python 3

requests (to send HTTP GET requests)

BeautifulSoup (bs4) (to parse HTML)

# 🚀 Features

Fetches webpage HTML via GET request

Parses and extracts all <h2> headlines

Saves output to headlines.txt

Includes error handling (try-except)

Easy to extend for other news websites

# 📄 File Structure
# 📁 Web-Scraper/
│-- news_scraper.py
│-- headlines.txt
│-- README.md

# ▶️ How to Run
1️⃣ Install dependencies
pip install requests beautifulsoup4

2️⃣ Run the script
python news_scraper.py

3️⃣ Output

A file named headlines.txt will be created containing all extracted news titles.

# 🧠 Key Concepts Learned

What is a GET request

HTML parsing

Using soup.find_all()

Working with tags & attributes

Writing to text files

HTTP status codes

Error handling using try-except

Basics of web scraping
