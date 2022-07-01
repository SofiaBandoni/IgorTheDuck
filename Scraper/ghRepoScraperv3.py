import requests
from bs4 import BeautifulSoup

# Indicar la url del repositorio a escrapear
github_url = 'https://github.com/SofiaBandoni/IgorTheDuck'

# Funcion que recorre el repositorio, se queda con los nombres y links de cada carpeta dentro del mismo
def get_repositories(github_url):
    url = github_url
    response = requests.get(url)
    response_code = response.status_code
    if response_code != 200:
        print("Error ocurred: " + str(response.status_code))
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    all_folders = dom.find_all(class_ = 'js-navigation-open Link--primary')
    dictionaries = []
    for folder in range(len(all_folders)):
        folder_name = (all_folders[folder].get("title"))
        folder_link = ("https://github.com" + all_folders[folder].get("href"))
        dictionaries.append({'Master Folder' : folder_name, 'Master Folder Link': folder_link})
    return(dictionaries)

subfolders_links = []
py_dicts = []
hql_dicts = []
          
def get_files(repos):  
    for repo in repos:
        object_type = str(type(repo))
        if 'dict' in object_type: 
            url = repo.get('Master Folder Link')
        else:
            url = repo
        response = requests.get(url)
        response_code = response.status_code
        if response_code != 200:
            print("Error ocurred: " + str(response.status_code))
            return
        html_content = response.content
        dom = BeautifulSoup(html_content, 'html.parser')
        files = dom.find_all(class_ = 'js-navigation-open Link--primary')
        for file in range(len(files)):
            link = ("https://github.com" + files[file].get("href"))
            raw_link = ("https://raw.githubusercontent.com/" + files[file].get("href")).replace("/blob", '')
            if ".py" in link:
                py_dicts.append({'Python Raw Links' : raw_link, 'Master Folder Link' : url})
            elif ".hql" in link:
                hql_dicts.append({'HQL Raw Links' : raw_link, 'Master Folder Link' : url})
            else: 
                subfolders_links.append(link)
                
if __name__ == '__main__':
    print('Started Scraping Main Repository...')
    repos = get_repositories(github_url)
    print("These are the folders links in main repository:" )
    print(repos)
    print("Started Scraping Folders In Main Repository...")
    files = get_files(repos)
    print("These are the files links:")
    while len(subfolders_links) > 0:
        get_files(subfolders_links)
        subfolders_links.clear()
        if len(subfolders_links) == 0:
            break
    print("Other Folders:")
    print(subfolders_links)
    print("Python Dictionaries")
    print(py_dicts)
    print("HQL Dictionaries")
    print(hql_dicts)