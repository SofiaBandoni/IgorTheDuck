import requests
from bs4 import BeautifulSoup

# Indicar la url del repositorio a escrapear
github_url = 'https://github.com/SofiaBandoni/IgorTheDuck'

# Funcion que recorre el repositorio y se queda con los links de cada carpeta dentro del mismo
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
    folders_links = []
    for folder in range(len(all_folders)):
        folder_name = (all_folders[folder].get("title"))
        print(folder_name)
        folders_links.append("https://github.com" + all_folders[folder].get("href"))       
    return(folders_links)


py_files_links = []
py_raw_links = []
hql_files_links = []
hql_raw_links = []
subfolders_links = []
          
def get_files(repos):  
    for repo in repos:
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
                py_files_links.append(link)
                py_raw_links.append(raw_link)
            elif ".hql" in link:
                hql_files_links.append(link)
                hql_raw_links.append(raw_link)
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
    print("Python:")
    print(py_files_links)
    print("Python Raw:")
    print(py_raw_links)
    print("Hql:")
    print(hql_files_links)
    print("Hql Raw:")
    print(hql_raw_links)
    print("Other Folders:")
    print(subfolders_links)