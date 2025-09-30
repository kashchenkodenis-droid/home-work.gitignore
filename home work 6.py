import requests

class WebPageScraper:
    def __init__(self, url):
        self.url = url

    def get_content(self):
        try:
            response = requests.get(self.url, timeout=5)
            response.raise_for_status()  # викликає помилку, якщо статус-код не 200
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Помилка при запиті: {e}"


scraper = WebPageScraper("https://www.example.com")
print(scraper.get_content())

scraper_bad = WebPageScraper("https://wrong-url.test")
print(scraper_bad.get_content())
