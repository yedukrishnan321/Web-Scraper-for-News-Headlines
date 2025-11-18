import requests
from bs4 import BeautifulSoup

def scrape_news_headlines():
    # Step 1: URL of the news website
    url = "https://www.bbc.com/news"  # You can replace with NDTV, CNN, etc.

    print("Fetching news headlines...")

    try:
        # Step 2: Fetch the HTML content
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Failed to load webpage! Status Code:", response.status_code)
            return

        # Step 3: Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 4: Extract <h2> headlines
        headlines = soup.find_all("h2")

        # Step 5: Write to text file
        with open("headlines.txt", "w", encoding="utf-8") as f:
            count = 1
            for h in headlines:
                title = h.get_text(strip=True)
                if title:
                    f.write(f"{count}. {title}\n")
                    count += 1

        print("Headlines scraped successfully!")
        print("Saved to file: headlines.txt")

    except Exception as e:
        print("Error occurred:", e)


# Run the program
if __name__ == "__main__":
    scrape_news_headlines()
