import requests
from bs4 import BeautifulSoup

# Indicar la url del repositorio a escrapear
github_url = 'https://github.com/SofiaBandoni/IgorTheDuck/blob/master/Folder1/query1.hql'

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
    code_lines = dom.find_all(class_ = 'blob-code blob-code-inner js-file-line')
    #print(code_lines)
    # code = []
    # for line in range(len(code_lines)):
    #     code.append(code_lines[line].find_all(class_ = 'pl-k'))
    #     code.append(code_lines[line].find_all(class_ = 'pl-c1'))    
    #print(code)
    for line in range(len(code_lines)):
        code = str((code_lines[line].find_all(class_ = 'pl-k'))).replace('<span class="pl-k">', '').replace('</span>','').replace('[','').replace(']','').replace(',', ' ')
        code2= str((code_lines[line].find_all(class_ = 'pl-c1'))).replace('<span class="pl-c1">', '').replace('</span>','').replace('[','').replace(']','').replace(',', ' ')
        
        print(code + code2)
        

    #return(links)


if __name__ == '__main__':
    get_code(github_url)
