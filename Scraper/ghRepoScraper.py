import requests
from bs4 import BeautifulSoup

def get_repositories():
    url = 'https://github.com/SofiaBandoni/IgorTheDuck'
    response = requests.get(url)
    response_code = response.status_code
    if response_code != 200:
        print("Error ocurred")
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    all_folders = dom.find_all(class_ = 'js-navigation-open Link--primary')
    print(all_folders)
    
if __name__ == '__main__':
    print('Started Scraping')
    get_repositories()
    