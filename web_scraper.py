import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Locate the elements containing the quotes and authors
            quotes = soup.find_all('span', class_='quote')
            authors = soup.find_all('span', class_='author')

            # Extract and print the quotes and authors
            for quote, author in zip(quotes, authors):
                print(f'"{quote.text}" - {author.text}')
        else:
            print(f"Failed to fetch content. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace this URL with the one you want to scrape
    target_url = "https://example-quotes-website.com"
    simple_web_scraper(target_url)
