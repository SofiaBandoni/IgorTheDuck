import requests
from bs4 import BeautifulSoup

# Indicar la url del repositorio a escrapear
github_url = 'https://raw.githubusercontent.com/SofiaBandoni/IgorTheDuck/master/Folder1/query1.hql'

# Armo una funcion que recorre el repositorio y va a devolver los links de cada carpeta dentro del mismo
def get_code(github_url):
    url = github_url
    response = requests.get(url)
    response_code = response.status_code
    if response_code != 200:
        print("Error ocurred: " + str(response.status_code))
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    print(dom)
    
if __name__ == '__main__':
    get_code(github_url)
    