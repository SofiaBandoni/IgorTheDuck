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
        folders_links.append("https://github.com" + all_folders[folder].get("href"))       
    return(folders_links)

          
def get_files(repos):
    py_files_links = []
    hql_files_links = []
    subfolders_links = []
    
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
            if ".py" in link:
                py_files_links.append(link)
            elif ".hql" in link:
                hql_files_links.append(link)
            else:
                subfolders_links.append(link)
    return(py_files_links, hql_files_links, subfolders_links)


if __name__ == '__main__':
    print('Started Scraping Main Repository...')
    repos = get_repositories(github_url)
    print("These are the folders links in main repository:" )
    print(repos)
    print("Started Scraping Folders In Main Repository...")
    files = get_files(repos)
    print("These are the files links:")
    print(files)
