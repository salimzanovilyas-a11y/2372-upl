import settings
import bs4

from .base import BaseParser

class CategoryParser(BaseParser):
    def get_categories(self):
        soup = self.get_soup()
        result = []
        nav_row = soup.find('div', class_='nav_row').find('ul')
        for item in nav_row.find_all('li')[:-3]:
            title = item.get_text(strip=True)
            href = item.find('a').get('href')

            result.append({
                'title': title,
                'href': settings.SITE_URL + href

            })
        return result




    def get_category_articles(self, category_url: str):
        soup = self.get_soup(category_url)
        wrapper = soup.find('div', id='content-block')
        return wrapper.find_all('div', class_='sh-news')


