from .base import BaseParser

class ArticleParser(BaseParser):
    def get_articles_data(self, category_articles):
        result = []

        for item in category_articles:
            title = item.find('h2').get_text()
            print(title)
            href = item.find('a').get('href')
            img = item.find('img').get('data-src')
            # img_name = img.split('/')[-1]
            # img_content = requests.get(img).content
            # with open(img_name, mode='wb') as file:
            #     file.write(img_content)
            # print(img)
            description = item.find('div', class_='sh-text').next.get_text(strip=True)
            side_date = item.find('div', class_='side-date').find_all('span')
            time = side_date[0].get_text()
            if len(side_date) == 2:
                comments = side_date[-1].get_text(strip=True)
            else:
                comments = '0'

            result.append({
                'title': title,
                'description': description,
                'time': time,
                'comments': comments,
                'href': href,
                **self.get_article_detail(href)
            })
        return result

    def get_article_detail(self, url):
        soup = self.get_soup(url)
        full_description = soup.find('div', {'itemprop': 'articleBody'}).get_text()
        return{
            'full_description': full_description
        }


