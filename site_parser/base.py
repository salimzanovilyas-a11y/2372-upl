import requests
import settings
import bs4


class BaseParser:
    def get_soup(self, url: str = settings.SITE_URL) -> bs4.BeautifulSoup:
        response = requests.get(url)
        response.raise_for_status()
        return bs4.BeautifulSoup(response.text, 'html.parser')