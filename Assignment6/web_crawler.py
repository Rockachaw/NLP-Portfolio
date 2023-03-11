import requests

from bs4 import BeautifulSoup


if __name__ == '__main__':
    starter_url = "https://en.wikipedia.org/wiki/Ross_Ulbricht"

    r = requests.get(starter_url)

    data = r.text
    soup = BeautifulSoup(data, features="html.parser")

    # write urls to a file
    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            print(link_str)

            # get all urls that contain 'Ulbright' or 'Silk' and don't contain 'wiki' or 'archive'
            if 'wiki' not in link_str and 'archive' not in link_str and ('ulbricht' in link_str or 'Ulbricht' in link_str or 'silk' in link_str or 'Silk' in link_str):
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    f.write(link_str + '\n')

    print('Web crawler finished.')
