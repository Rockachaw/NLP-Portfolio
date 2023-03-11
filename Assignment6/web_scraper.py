import os
import shutil

from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen


def scrape_text(filename):

    # create pages directory
    pages_dir = os.getcwd() + '\\pages'
    if os.path.exists(pages_dir):
        shutil.rmtree(pages_dir)
    os.makedirs(pages_dir)

    # get urls from file
    file = open(filename, 'r')
    urls = file.readlines()

    for url in urls:
        try:
            response = urlopen(url)

            # attempt to detect the correct charset
            content_type = response.getheader('Content-Type')
            charset = 'utf-8'
            if 'charset' in content_type.lower():
                charset = content_type.split('charset=')[-1]

            html = response.read()
            html = html.decode(charset)

            soup = BeautifulSoup(html, 'html.parser')

            # turn url into a legal filename
            unique_name = url.replace("://", "_").replace(".", "_").replace("/", "_").replace("=", "_").replace("?", "_").replace("\n", "")
            page_file = open(pages_dir + '\\' + unique_name + '.txt', 'w')

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()  # rip it out

            # extract paragraph tags
            for p in soup.select('p'):
                try:
                    page_file.write(p.text)
                except UnicodeEncodeError as err:
                    print(f"Unicode Encode error occurred: {err}")

            print("Created " + unique_name)
            page_file.close()

        # triggers on http error (mostly 403: forbidden)
        except HTTPError as err:
            print(f"HTTP error occurred: {err}")

        # triggers on incorrect character set
        except UnicodeDecodeError as err:
            print(f"Unicode Decode error occurred: {err}")


if __name__ == '__main__':
    scrape_text('urls.txt')
    print('Web scraper finished.')
