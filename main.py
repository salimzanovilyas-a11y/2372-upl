from site_parser .category import CategoryParser
from site_parser.article import ArticleParser
import json
import time


def main():
    final_result = {}

    category_parser = CategoryParser()
    article_parser = ArticleParser()

    start = time.time()
    categories = category_parser.get_categories()
    for category in categories:
        category_title = category.get('title')
        print('[CATEGORY]', category_title)
        category_url = category.get('href')
        category_articles = category_parser.get_category_articles(category_url)
        articles_data = article_parser.get_articles_data(category_articles)

        final_result[category_title] = articles_data
        with open('upl.json', mode='w', encoding='utf=8') as file:
            json.dump(final_result, file, ensure_ascii=False, indent=4)

        print(time.time() - start)


main()