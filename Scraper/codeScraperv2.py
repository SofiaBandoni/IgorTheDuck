import requests
from bs4 import BeautifulSoup
from sql_metadata import Parser

# Indicar la url del repositorio a escrapear
github_url = 'https://raw.githubusercontent.com/SofiaBandoni/IgorTheDuck/master/Folder1/query1.hql'


def get_raw_code(github_url):
    url = github_url
    response = requests.get(url)
    response_code = response.status_code
    if response_code != 200:
        print("Error ocurred: " + str(response.status_code))
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    return(dom)
    
def get_sql_tables(raw_code):
    tables = Parser(str(raw_code)).tables
    return(tables)

if __name__ == '__main__':
    raw_code = get_raw_code(github_url)
    print(raw_code)
    sql_tables = get_sql_tables(raw_code)
    print(sql_tables)
    