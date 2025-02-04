import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


class WordleScraper:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("WORDLE_ANSWER_SITE_URL")
        if not self.url:
            raise ValueError("WORDLE_ANSWER_SITE_URL environment variable is not set.")

    def get_site_content(self):
        """
        Fetches the content of the Wordle answer site.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as err:
            raise RuntimeError(f"Error fetching site content: {err}")

    def get_wordle_for_today(self):
        """
        Scrapes and returns the Wordle of the day.
        """
        content = self.get_site_content()
        if not content:
            raise ValueError("Failed to fetch content from the site.")

        soup = BeautifulSoup(content, "lxml")
        wordle_paragraph = soup.find("p", attrs={"data-characters": "45"})
        if not wordle_paragraph:
            raise ValueError("Could not find the Wordle answer paragraph in the page.")

        wordle_answer = wordle_paragraph.find("strong")
        if not wordle_answer:
            raise ValueError("Could not find the Wordle answer in the paragraph.")

        return wordle_answer.get_text().strip()


if __name__ == "__main__":
    try:
        scraper = WordleScraper()
        wordle = scraper.get_wordle_for_today()
        print("Wordle of the day is:", wordle)
    except Exception as err:
        print("Error:", err)